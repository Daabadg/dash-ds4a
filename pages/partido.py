#libraries
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import html , dcc, callback, Input, Output, State
from sklearn.feature_extraction import img_to_graph

# dash-labs plugin call, menu name and route
register_page(__name__, path="/partido")

from components.maps.mapcol_departamentos import mapcol_departamentos

from components.maps.mapsample import mapsample
from data.dataframes.database import listaPartidos
from components.plots.PartPlots import PartPlots
from components.sampledf.model import df_maptest
from components.table.table import table
from components.kpi.kpibadge import kpibadge

kpi1 = kpibadge('1500', 'Departamento con mas procesos', 'Bogota')


mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',df_maptest)

imgPartido = PartPlots('Procesos por partido', listaPartidos,'PACTO HISTORICO')

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                html.H1("Partidos", className='title ml-2')
            ])
        ]),
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el partido'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_partido",
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
                        id="id_selector_senador",multi=False, placeholder="Senador"
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
                dbc.Row(html.Div(id="tag-senadores")),
                dbc.Row(html.Div(id="tag-casos")),
        ]),dbc.Col([
                    imgPartido.display()   
        ],id="plot-part"),
        dbc.Col([
                    mapa_colombia_departamentos.display()   
        ])
        ])
    ],className='container-fluid',style={'margin':'auto','width':'100%'}
)


@callback(
Output("id_selector_senador","options"),
Input("id_selector_partido","value")
)
def senator_dropdown(partido):
    df_filtro = listaPartidos[listaPartidos['Partido']==partido]['Senadores'].unique()
    return [{"label": i, "value": i} for i in df_filtro]


@callback(
    Output("tag-senadores","children"),
    Input("id_selector_partido","value")
)
def partyMembers(partido):
    cuenta = listaPartidos[listaPartidos['Partido']==partido]['Senadores'].count()
    kpi = kpibadge(cuenta, 'No. Senadores', 'success')
    return [kpi.display()]

@callback(
Output("plot-part","children"),
Input("id_selector_partido","value")
)

def update_plot(partido):
        #df_filtrado = imgPartido.df[imgPartido.df['Partido']==partido]
        #df_filtrado = df_filtrado[df_filtrado['COUNT']]
        imgPartido.partido = partido
        nuevo_plot = imgPartido.display()
        #mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado )
        #nuevo_mapa = mapa_filtrado.display()
        return [nuevo_plot]