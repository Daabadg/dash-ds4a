import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/")

from components.kpi.kpibadge import kpibadge
from components.kpi.kpiplot import kpiplot
from components.table.table import table
from components.sampledf.model import df_costos
from components.maps.mapsample import mapsample
from data.dataframes.databaseDA import listaPartidos
from components.plots.PartPlots import PartPlots
from components.kpi.kpibadgeAMD import kpibadgeAMD

kpi3plot = kpiplot('Total KPI', df_costos['VALUE'], 'count')
kpi4plot = kpiplot('Total User', df_costos['VALUE'], 'count')

kpi1 = kpibadgeAMD('120', 'Senador con mas procesos', 'GUSTAVO BOLIVAR MORENO')
kpi2 = kpibadgeAMD('1500', 'Departamento con mas procesos', 'Bogota')


mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

imgPartido = PartPlots('Procesos por partido', listaPartidos,'PACTO HISTORICO')

params1 = {
            'title': 'Users', 
            'description': 'Tabla de lista de usuarios',
            'columns': ['ID', 'CIUDAD', 'TIPO', 'FECHA']
}
tablaventas = table(df_costos,params1)


layout=  dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                #mapa_ejemplo.display()
                imgPartido.display()


            ],id="plot-part", md=8), 
            dbc.Col([
                dbc.Row([
                    dbc.Col([ kpi1.display()]),
                    dbc.Col([ kpi2.display()])
                ]),
                dbc.Row([
                    dbc.Col([ kpi1.display()]),
                    dbc.Col([ kpi1.display()])
                ]),
            ]), 
        ]),
        dbc.Row([
            dbc.Col([
                tablaventas.display()
            ], className='card')
        ])
        
      
    ]
)  