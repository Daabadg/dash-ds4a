import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/senador")

from dash import  dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

from data.dataframes.database import listaPartidos
from data.dataframes.database import conteoProcesos
from data.dataframes.database import personaProcesosTipo
from data.dataframes.database import personaProcesosDepartamento



from components.maps.mapsample import mapsample
from components.cardImg.cardImg import cardImg
from components.kpi.kpibadgeAMDsencilla import kpibadgeAMDsencilla
from components.plots.plotGroupone import plotGroupone
from components.plots.plotGrouptwo import plotGrouptwo
from components.plots.plotTwo import plotTwo
#df = pd.read_csv(r'C:\Users\Andrea\Documents\Varios\DS4A\Dash\data\Procesos.csv',sep=";")
#df_senador = df.groupby("DEPARTAMENTO")
#print("past groupby")
#fig = px.bar(df_senador['Número de Radicación'].count().sort_values(ascending=False).head(10))
mapa_ejemplo = mapsample('This is my custom map', 'div_samplemap')

#Variables obtenidas de bases
SumaPartido = conteoProcesos.groupby(['PARTIDO']).sum()
SumaPartido.reset_index(inplace = True)

SumaTipoProseco = personaProcesosTipo.groupby(['PERSON_ID']).sum()
SumaTipoProseco.reset_index(inplace = True)


PersonProcDepto = personaProcesosDepartamento[personaProcesosDepartamento['PERSON_NAME']=='GUSTAVO BOLIVAR MORENO']
#Senador = "AIDA MARINA QUILCUE VIVAS"
#TotalSen, TotalPart, TotalDemandado, TotalDemandante = GetInfoSen(conteoProcesos, SumaPartido, SumaTipoProseco, Senador)

imgDepartamento = plotTwo('Procesos por partido', PersonProcDepto,'DEPARTAMENTO','CANTIDAD_PROCESOS_PUBLICOS','CANTIDAD_PROCESOS_PRIVADOS')

#Llamado de componentes
#cardSen = cardImg("AIDA MARINA QUILCUE VIVAS", "AIDA MARINA QUILCUE VIVAS")


button_group_Sen = dbc.ButtonGroup(
    [
        dbc.Button([
                    'Casos'
                ],id="btt_casos"),
        dbc.Button([
                    'Departamento'
                ],id="btt_depto"),
        dbc.Button([
                    'Serie de tiempo'
                ],id="btt_Tiempo"),
    ],
)

layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1("Senador", className='title ml-2')
            ])
        ]),
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el partido'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_partidoS",
                        options=[
                            {"label": i, "value": i} for i in listaPartidos.Partido.unique()
                        ],multi=False, placeholder="Partido"
                        )
                    ])
                ]),
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el senador'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_senadorS",multi=False, placeholder="Senador"
                        )
                    ])
                ])
            ]),
        ],className="card"),
    dbc.Row([
        dbc.Col([
            #html.Div(id="Cardsen"),
            html.Div(id="Card-Img"),
            html.Div(id="kpi-total"),
            html.Div(id="kpi-porcentaje")
        ], md=3),

        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(id="kpi-demandado"),
                ],md=6),
                dbc.Col([
                    html.Div(id="kpi-demandante"),
                ],md=6)
            ], className='h-5'),
            dbc.Row([
                html.Div([
                    imgDepartamento.display()
                ],id='graficacentral'),            
                ],justify = 'center'),
            dbc.Row([
                dbc.Col([
                    button_group_Sen
                ],md=7)
                
            ],justify = 'center'),
        ], className='card', md=8),
    ])
    
])


#callbacks

# Callback para el filtrado de la lista de senadores
@callback(
Output("id_selector_senadorS","options"),
Input("id_selector_partidoS","value")
)
def senator_dropdown(partido):
    df_filtro = listaPartidos[listaPartidos['Partido']==partido]['Senadores'].unique()
    return [{"label": i, "value": i} for i in df_filtro]

#Callback para el filtrado del senador
 
@callback(
    Output("kpi-total","children"),
    Output("kpi-porcentaje","children"),
    Output("kpi-demandado","children"),
    Output("kpi-demandante","children"),
    Output("Card-Img","children"),
    Output("graficacentral","children"),
    Input("id_selector_senadorS","value")
)
def actKPI(senador):
    Senproc = conteoProcesos[conteoProcesos["PERSON_NAME"] == senador]
    cuentaSen = int(Senproc.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']) + Senproc.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']
    Partproc = SumaPartido[SumaPartido['PARTIDO']==Senproc.iloc[0]['PARTIDO']]
    cuentaPar = int(Partproc.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']) + Partproc.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']
    SenprocTipo = SumaTipoProseco[SumaTipoProseco['PERSON_ID']== Senproc.iloc[0]['PERSON_ID']]
    cuentaDemandado = SenprocTipo.iloc[0]['ES_DEMANDADO']
    cuentaDemandante = SenprocTipo.iloc[0]['ES_DEMANDANTE']
    partido = Senproc.iloc[0]['PARTIDO']
    descripcion = 'Es un escritor, empresario, periodista, guionista y político colombiano,'

    
    kpi1 = kpibadgeAMDsencilla(str(cuentaSen), 'Total casos')
    kpi2 = kpibadgeAMDsencilla(str(round((cuentaSen*100)/cuentaPar,2)), '% Casos del partido')
    kpi3 = kpibadgeAMDsencilla(str(cuentaDemandado), 'Casos como demandado')
    kpi4 = kpibadgeAMDsencilla(str(cuentaDemandante), 'Casos como demandante')
    cardSen = cardImg(senador, senador,partido,descripcion)

    PersonProcDepto = personaProcesosDepartamento[personaProcesosDepartamento['PERSON_NAME']==senador]
    imgDepartamento.data = PersonProcDepto
    
            

    return kpi1.display(), kpi2.display(), kpi3.display(), kpi4.display(), cardSen.display(), imgDepartamento.display()