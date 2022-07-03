from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class barPlots:
    """ A class to represent plot"""
    def __init__(self,label:str, data, partido:str,x:str,y:str):
        """Constructs all the attributes for kpiplot class"""
        self.label = label
        self.data = data
        self.partido = partido
        self.x = x
        self.y = y

        #self.cuenta = self.data.groupby(['Partido']).count()
        #self.cuenta = self.cuenta.reset_index()
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
        df = self.data[self.data['PARTIDO'] == self.partido]
        fig = px.bar(df, x=self.x, y=self.y)
        
        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        layout = html.Div(
            [
             html.H4([self.label]),
             #html.Div(self.label,className='bar-plot'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=barPlots.figura(self)),
            ],className='card'
        )
        return layout