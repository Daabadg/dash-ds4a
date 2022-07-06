import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/senador")

from dash import  dcc, html, Input, Output, callback, State, callback_context
import plotly.express as px
import pandas as pd

from data.dataframes.database import listaPartidos
from data.dataframes.database import conteoProcesos
from data.dataframes.database import personaProcesosTipo
from data.dataframes.database import personaProcesosDepartamento
from data.dataframes.database import personProcesoDetails


from components.maps.mapsample import mapsample
from components.cardImg.cardImg import cardImg
from components.kpi.kpibadgeAMDsencilla import kpibadgeAMDsencilla
from components.plots.plotGroupone import plotGroupone
from components.plots.plotGrouptwo import plotGrouptwo
from components.plots.plotTwo import plotTwo
from components.plots.serieDeTiempo import serieDeTiempo
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

listaPartidosC = listaPartidos.copy()
conteoProcesosC = conteoProcesos.copy()
personaProcesosTipoC = personaProcesosTipo.copy()
personaProcesosDepartamentoC = personaProcesosDepartamento.copy()
personProcesoDetailsC = personProcesoDetails.copy()

#Senador = "AIDA MARINA QUILCUE VIVAS"
#TotalSen, TotalPart, TotalDemandado, TotalDemandante = GetInfoSen(conteoProcesos, SumaPartido, SumaTipoProseco, Senador)


#Llamado de componentes
#cardSen = cardImg("AIDA MARINA QUILCUE VIVAS", "AIDA MARINA QUILCUE VIVAS")


button_group_Sen = dbc.ButtonGroup(
    [
        dbc.Button([
                    'Tipo de proceso'
                ],id="btt_casos"),
        dbc.Button([
                    'Departamento'
                ],id="btt_depto"),
        dbc.Button([
                    'Fecha'
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
                        ],value='PACTO HISTORICO'
                        ,multi=False, placeholder="Partido"
                        )
                    ])
                ]),
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el senador'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_senadorS",value='GUSTAVO BOLIVAR MORENO',multi=False, placeholder="Senador"
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
                html.Div(id="graficacentral"),           
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
    Input("id_selector_senadorS","value")
)
def actKPI(senador):
    Senproc = conteoProcesosC[conteoProcesosC["PERSON_NAME"] == senador]
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
    kpi3 = kpibadgeAMDsencilla(str(cuentaDemandado), 'Procesos como demandado')
    kpi4 = kpibadgeAMDsencilla(str(cuentaDemandante), 'Procesos como demandante')
    cardSen = cardImg(senador, senador,partido,descripcion)

    return kpi1.display(), kpi2.display(), kpi3.display(), kpi4.display(), cardSen.display()




@callback(
Output("graficacentral","children"),
Input("id_selector_senadorS","value"),
Input("btt_casos","n_clicks"),
Input("btt_depto","n_clicks"),
Input("btt_Tiempo","n_clicks")
)
def update_plot(senador,btn1,btn2,btn3):
    
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btt_casos' in changed_id:
        filt2 = personProcesoDetailsC[personProcesoDetailsC['PERSON_NAME'] == senador]
        filt2['TIPO_PROCESO'] = filt2['TIPO_PROCESO'].str.upper()
        filt2 = filt2.groupby(['TIPO_PROCESO']).count()
        filt2.reset_index(inplace = True)
        imgCasos = plotGroupone('Tipos de procesos',filt2,'TIPO_PROCESO','TIPO_PROCESO','ID_PROCESO')
        nuevo_plot = imgCasos.display()
    elif 'btt_depto' in changed_id:
        PersonProcDepto = personaProcesosDepartamentoC[personaProcesosDepartamentoC['PERSON_NAME']==senador]
        imgDepartamento = plotTwo('Procesos por partido', PersonProcDepto,'DEPARTAMENTO','CANTIDAD_PROCESOS_PUBLICOS','CANTIDAD_PROCESOS_PRIVADOS')
        nuevo_plot = imgDepartamento.display()
    elif 'btt_Tiempo' in changed_id:
        filt = personProcesoDetailsC[personProcesoDetailsC['PERSON_NAME'] == senador]
        imgSerieTiempo = serieDeTiempo('Procesos',filt,'FECHA_PROCESO')
        nuevo_plot = imgSerieTiempo.display()
    else:
        PersonProcDepto = personaProcesosDepartamentoC[personaProcesosDepartamentoC['PERSON_NAME']==senador]
        imgDepartamento = plotTwo('Procesos por partido', PersonProcDepto,'DEPARTAMENTO','CANTIDAD_PROCESOS_PUBLICOS','CANTIDAD_PROCESOS_PRIVADOS')
        nuevo_plot = imgDepartamento.display()
    return [nuevo_plot]