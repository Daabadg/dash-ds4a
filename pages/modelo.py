#libraries
from telnetlib import OUTMRK
from traceback import print_tb
from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import html , dcc, callback, Input, Output, State, callback_context

# dash-labs plugin call, menu name and route
register_page(__name__, path="/modelo")

from components.maps.mapcol_departamentos import mapcol_departamentos

from data.dataframes.database import listaPartidos, partidoProcesoFecha
from components.plots.plotModelo import plotModelo

partidoProcesoFechaC = partidoProcesoFecha.copy()

layout= html.Div(
    [
        dbc.Row([
            dbc.Col([
                html.H1("Modelo", className='title ml-2')
            ])
        ]),
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div(['Seleccione el partido'],className="mb-2 selector-label"),
                        dcc.Dropdown(
                        id="id_selector_partidoM",
                        options=[
                            {"label": i, "value": i} for i in listaPartidos.Partido.unique()
                        ],value="PACTO HISTORICO",multi=False, placeholder="Partido"
                        )
                    ])
                ]),

            ]),         
        ],className="card"),
        
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Div(id="plot-Modelo")
                    ],#className="h-75"
                    ),
                ],className='card m-0'),
        ])
    ],className='container-fluid',style={'margin':'auto','width':'100%'}
)



# Callback para el conteo de senadores por partido
@callback(
    Output("plot-Modelo","children"),
    Input("id_selector_partidoM","value")
)
def partyMembers(partido):
    plotmodelo = plotModelo('Modelo',partidoProcesoFechaC,partido)

    return plotmodelo.display()
