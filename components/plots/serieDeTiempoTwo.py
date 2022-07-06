from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class serieDeTiempoTwo:
    """ A class to represent plot"""
    def __init__(self,label, data_, fecha,color):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        self.data = pd.DataFrame(data_)                             #Data that is going to graph
        #self.partido = partido
        self.data['fecha_Mes'] = pd.to_datetime(self.data[str(fecha)]).dt.to_period(freq = 'M')
        self.cuenta = self.data.groupby(['fecha_Mes']).count()     #Group by and filtter applied
        self.color = color
    
        #self.filt = self.cuenta[self.cuenta['Partido']==str(partido)]
        #elf.filt.replace(to_replace =["M", "F"], value =["Masculino","Femenino"],inplace=True)
        #self.cuenta_partido = self.data.groupby(partido,["Genero"]).count()
    
    #@staticmethod
    def figura(self):
        '''
        datadict = [dict(x=self.cuenta.Senadores,type='histogram')]
        layout = dict(
            autosize=True,
            margin=dict(l=1, r=0, t=0, b=0, pad=0),
            height=120,
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis_visible=False,
            yaxis_showticklabels=False,
            xaxis=dict(
                title='',
                type='linear'
            ),
        )
        
        fig=dict(data=datadict,layout=layout)
        '''
        #print(self.cuenta)
        #Create figure with specifics
        fig = px.line(self.cuenta, x=self.cuenta.index.to_timestamp(), y='ID_PROCESO',color_discrete_sequence=px.colors.qualitative.Set2,color=self.color)
        #datadict = [dict(x=self.cuenta,type='bar')]
        
        

        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=serieDeTiempoTwo.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ]
        )
        return layout