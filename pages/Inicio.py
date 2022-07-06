import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/")

from components.kpi.kpibadge import kpibadge
from components.kpi.kpiplot import kpiplot
from components.table.table import table
from components.sampledf.model import df_costos
from components.maps.mapsample import mapsample
from data.dataframes.database import listaPartidos
from data.dataframes.database import conteoProcesos
from components.plots.plotGroupone import plotGroupone
from components.plots.plotGrouptwo import plotGrouptwo
from components.kpi.kpibadgeAMD import kpibadgeAMD

kpi3plot = kpiplot('Total KPI', df_costos['VALUE'], 'count')
kpi4plot = kpiplot('Total User', df_costos['VALUE'], 'count')




mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

#imgPartido = plotGroupone('Procesos por partido', listaPartidos,'Partido','Partido','Senadores')
imgPartidoGenero = plotGrouptwo('Procesos por partido', conteoProcesos,'PARTIDO','GENERO','PARTIDO','CANTIDAD_PROCESOS_PUBLICOS')

maxProcSenPu = conteoProcesos[conteoProcesos["CANTIDAD_PROCESOS_PUBLICOS"] == conteoProcesos["CANTIDAD_PROCESOS_PUBLICOS"].max()]
maxProcSenPr = conteoProcesos[conteoProcesos["CANTIDAD_PROCESOS_PRIVADOS"] == conteoProcesos["CANTIDAD_PROCESOS_PRIVADOS"].max()]

kpi1 = kpibadgeAMD(str(maxProcSenPu.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']), 'Senador con mas procesos publicos', str(maxProcSenPu.iloc[0]['PERSON_NAME']))
kpi2 = kpibadgeAMD(str(maxProcSenPr.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']), 'Senador con mas procesos privados', str(maxProcSenPr.iloc[0]['PERSON_NAME']))


#kpi1 = kpibadgeAMD("640", 'Senador con mas procesos publicos', "RODOLFO HERNÁNDEZ SUÁREZ")
params1 = {
            'title': 'Procesos', 
            'description': 'Tabla de lista de Procesos',
            'columns': ['PERSON_ID', 'PERSON_NAME', 'GENERO', 'PARTIDO',
       'CANTIDAD_PROCESOS_PUBLICOS', 'CANTIDAD_PROCESOS_PRIVADOS']
}
tablaprocesos = table(conteoProcesos,params1)


layout=  dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                #mapa_ejemplo.display()
                #imgPartido.display(),
                imgPartidoGenero.display()
            ], className='card',id="plot-part", md=8), 
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
                tablaprocesos.display()
            ], className='card')
        ])
        
      
    ]
)  