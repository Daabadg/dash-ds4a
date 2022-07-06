import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/comparacion")

from dash import  dcc, html, Input, Output, callback, State, callback_context
import plotly.express as px
import pandas as pd

from data.dataframes.database import listaPartidos
from data.dataframes.database import conteoProcesos
from data.dataframes.database import personaProcesosTipo
from data.dataframes.database import personaProcesosDepartamento
from data.dataframes.database import personProcesoDetails



from components.kpi.kpibadge import kpibadge
from components.kpi.kpiplot import kpiplot
from components.table.table import table
from components.sampledf.model import df_costos
from components.maps.mapsample import mapsample

from components.plots.plotTwoxTwo import plotTwoxTwo
from components.kpi.kpibadgeAMD import kpibadgeAMD
from components.cardImg.cardImg import cardImg
from components.plots.piechartSen import piechartSen
from components.plots.serieDeTiempoTwo import serieDeTiempoTwo

personaProcesosDepartamento['Total procesos'] = personaProcesosDepartamento['CANTIDAD_PROCESOS_PUBLICOS'] + personaProcesosDepartamento['CANTIDAD_PROCESOS_PRIVADOS']

mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

listaPartidosC = listaPartidos.copy()
conteoProcesosC = conteoProcesos.copy()
personaProcesosTipoC = personaProcesosTipo.copy()
personaProcesosDepartamentoC = personaProcesosDepartamento.copy()
personProcesoDetailsC = personProcesoDetails.copy()

params1 = {
            'title': 'Users', 
            'description': 'Tabla de lista de usuarios',
            'columns': ['ID', 'CIUDAD', 'TIPO', 'FECHA']
}
tablaventas = table(df_costos,params1)

button_group_Comp = dbc.ButtonGroup(
    [
        dbc.Button([
                    'Departamento'
                ],id="btt_deptoC"),
        dbc.Button([
                    'Fecha'
                ],id="btt_TiempoC"),
    ],
)

layout=  dbc.Container(
    [
         dbc.Row([
            dbc.Col([
                html.H1("Comparar", className='title ml-2')
            ])
        ]),
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione un senador o senadora'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_senador1",
                        options=[
                            {"label": i, "value": i} for i in listaPartidos.Senadores.unique()
                        ],value='GUSTAVO BOLIVAR MORENO'
                        ,multi=False, placeholder="Partido"
                        )
                    ])
                ]),
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione un senador o senadora'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_senador2",
                        options=[
                            {"label": i, "value": i} for i in listaPartidos.Senadores.unique()
                        ],value='ALEXANDER LOPEZ MAYA'
                        ,multi=False, placeholder="Senador"
                        )
                    ])
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Button([
                        'Filtrar'
                    ],id="id_filtrar")
                ],class_name="d-flex justify-content-end mt-2"),
            ]),
        ],className="card"),
        

        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Div(id="Card-Img1"),
                ]),
            ], md=2), 
            dbc.Col([
                dbc.Row([
                    html.Div(id="Card-Img2"),
                ]),
            ],md=2), 
            dbc.Col([
                dbc.Row([
                    html.Div(id="plot-comp"),
                ]),
                dbc.Row([
                    dbc.Col([
                        button_group_Comp
                ],md=7)
                ],justify = 'center'),
            ], className='card',md=7), 
        ]),
        dbc.Row([   
            dbc.Col([
               
                dbc.Row([
                    html.Div(id="Pie-Sen1"),
                ]),
            ], md=3), 
            dbc.Col([
                dbc.Row([
                    html.Div(id="Pie-Sen2"),
                ]),
            ],md=3), 
            dbc.Col([
                dbc.Row([
                    html.Div(id="badge-sen1"),
                ]),
            ],md=3), 
            dbc.Col([
                dbc.Row([
                    html.Div(id="badge-sen2"),
                ]),
            ],md=3),
        ]),

        dbc.Row([
            dbc.Col([
                tablaventas.display()
            ], className='card')
        ])
        
      
    ]
)  

@callback(
        [Output("Card-Img1", 'children'),
         Output("Card-Img2", 'children'),
         Output("Pie-Sen1", 'children'),
         Output("Pie-Sen2", 'children'),
         Output("badge-sen1", 'children'),
         Output("badge-sen2", 'children'),], 
        [State("id_selector_senador1","value"),
         State("id_selector_senador2","value"),
         Input("id_filtrar", "n_clicks"),
                
        ]
    )
def update_map(senador1,senador2,nclicks):

    Sen1proc = conteoProcesosC[conteoProcesosC["PERSON_NAME"] == senador1]
    cuentaSen1 = int(Sen1proc.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']) + Sen1proc.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']
    partido1 = Sen1proc.iloc[0]['PARTIDO']
    descripcion1 = 'Es un escritor, empresario, periodista, guionista y político colombiano,'

    Sen2proc = conteoProcesosC[conteoProcesosC["PERSON_NAME"] == senador2]
    cuentaSen2 = int(Sen2proc.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']) + Sen2proc.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']
    partido2 = Sen2proc.iloc[0]['PARTIDO']
    descripcion2 = 'Es un escritor, empresario, periodista, guionista y político colombiano,'
    
    cardSen1 = cardImg(senador1, senador1,partido1,descripcion1)
    cardSen2 = cardImg(senador2, senador2,partido2,descripcion2)
    pieSen1 = piechartSen('Tipo de proceso',Sen1proc, senador1)
    pieSen2 = piechartSen('Tipo de proceso',Sen2proc, senador2)
   
    kpisen1 = kpibadgeAMD(str(cuentaSen1), 'Total procesos', senador1)
    kpisen2 = kpibadgeAMD(str(cuentaSen2), 'Total procesos', senador2)



    return [cardSen1.display(),cardSen2.display(),pieSen1.display(),pieSen2.display(),kpisen1.display(),kpisen2.display()]


@callback(
Output("plot-comp", 'children'),
[State("id_selector_senador1","value"),
State("id_selector_senador2","value"),
Input("btt_deptoC","n_clicks"),
Input("btt_TiempoC","n_clicks"),
])
def update_plot(senador1,senador2,btn1,btn2):
    
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btt_deptoC' in changed_id:
        imgProcDepto = plotTwoxTwo('Procesos por partido', personaProcesosDepartamentoC,senador1,senador2,'DEPARTAMENTO','Total procesos','PERSON_NAME')
        nuevo_plot = imgProcDepto.display()
    elif 'btt_TiempoC' in changed_id:
        
        filt2 = personProcesoDetailsC.query("PERSON_NAME == '"+str(senador1)+ "' | PERSON_NAME == '"+ str(senador2)+"'")
        
        imgTiempo = serieDeTiempoTwo('Procesos',filt2,'FECHA_PROCESO','PERSON_NAME')
        nuevo_plot = imgTiempo.display()
    else:
        imgProcDepto = plotTwoxTwo('Procesos por partido', personaProcesosDepartamentoC,senador1,senador2,'DEPARTAMENTO','Total procesos','PERSON_NAME')
        nuevo_plot = imgProcDepto.display()
    return [nuevo_plot]