#libraries
from telnetlib import OUTMRK
from traceback import print_tb
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import html , dcc, callback, Input, Output, State, callback_context
from sklearn.feature_extraction import img_to_graph

# dash-labs plugin call, menu name and route
register_page(__name__, path="/partido")

from components.maps.mapcol_departamentos import mapcol_departamentos

from data.dataframes.database import listaPartidos,conteoProcesos,depPartidos
from components.plots.PartPlots import PartPlots
from components.plots.piechart import piechart
from components.kpi.kpibadge import kpibadge
from components.plots.barPlots import barPlots

# PIECHART POR GENERO
pieGenero = piechart("Genero",listaPartidos,"PACTO HISTORICO")

# BAR PLOT DEPARTAMENTO
barDepartamento = barPlots("Departamentos",depPartidos,"PACTO HISTORICO","DEPARTAMENTO","COUNT")

# MAPA COLOMBIA
mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',depPartidos)


#imgPartido = PartPlots('Procesos por partido', listaPartidos,'PACTO HISTORICO')

# Botones para elegir graficas
button_group_par = dbc.ButtonGroup(
    [
        dbc.Button([
                    'Edad'
                ],id="btt_edad"),
        dbc.Button([
                    'Genero'
                ],id="btt_genero"),
        dbc.Button([
                    'Departamento'
                ],id="btt_dpto"),
    ],
)

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
                        ],value="PACTO HISTORICO",multi=False, placeholder="Partido"
                        )
                    ])
                ]),
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el senador'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_senador",value='GUSTAVO BOLIVAR MORENO',multi=False, placeholder="Senador"
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
                dbc.Row(html.Div(id="tag-registros")),
        ],width=2),
            dbc.Col([
                dbc.Row([
                    html.Div(id="plot-part")
                    ],#className="h-75"
                    ),
                dbc.Row([
                    dbc.Col([
                        button_group_par
                        ],md=9)
                        ],justify = 'center')
                        ],width=4,className='card m-0'),
            dbc.Col([
                    html.Div(id="map-partidos")  
                ],width=6)
        ])
    ],className='container-fluid',style={'margin':'auto','width':'100%'}
)

# Callback para el filtrado de la lista de senadores
@callback(
Output("id_selector_senador","options"),
Input("id_selector_partido","value")
)
def senator_dropdown(partido):
    df_filtro = listaPartidos[listaPartidos['Partido']==partido]['Senadores'].unique()
    return [{"label": i, "value": i} for i in df_filtro]

# Callback para el conteo de senadores por partido
@callback(
    Output("tag-senadores","children"),
    Input("id_selector_partido","value")
)
def partyMembers(partido):
    cuenta = listaPartidos[listaPartidos['Partido']==partido]['Senadores'].count()
    kpi = kpibadge(cuenta, 'No. Senadores', 'success')
    return [kpi.display()]

# Callback para el conteo de registros por partido
@callback(
    Output("tag-registros","children"),
    Input("id_selector_partido","value")
)
def regCount(partido:str):
    party = partido
    cuenta = conteoProcesos[conteoProcesos['PARTIDO']==party][['CANTIDAD_PROCESOS_PRIVADOS','CANTIDAD_PROCESOS_PUBLICOS']].sum()
    cuenta = sum(cuenta)
    kpi = kpibadge(cuenta, 'No. Procesos', 'success')
    return [kpi.display()]

# Callback para el mapa
@callback(
    Output("map-partidos","children"),
    Input("id_selector_partido","value")
)
def mapSen(partido:str):
    df = mapa_colombia_departamentos.df
    df_filtrado = df[df['PARTIDO']==partido]
    #df_filtrado['COUNT'] = df_filtrado['CANTIDAD_PROCESOS_PUBLICOS']+df_filtrado['CANTIDAD_PROCESOS_PRIVADOS']
    df_filtrado = df_filtrado[['DEPARTAMENTO','COUNT','COD_DPTO']]
    mapa_colombia_departamentos.df = df_filtrado
    nuevo_mapa = mapa_colombia_departamentos.display()
    mapa_colombia_departamentos.df = depPartidos
    return [nuevo_mapa]
    
# Boton de genero
@callback(
Output("plot-part","children"),
Input("id_selector_partido","value"),
Input("btt_genero","n_clicks"),
Input("btt_edad","n_clicks"),
Input("btt_dpto","n_clicks")
)
def update_plot(partido,btn1,btn2,btn3):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btt_genero' in changed_id:
        pieGenero.partido = partido
        nuevo_plot = pieGenero.display()
    elif 'btt_edad' in changed_id:
        print('Button 2 was most recently clicked')
    elif 'btt_dpto' in changed_id:
        barDepartamento.partido = partido
        nuevo_plot = barDepartamento.display()
    else:
        pieGenero.partido = partido
        nuevo_plot = pieGenero.display()
    return [nuevo_plot]

# Boton de departamento