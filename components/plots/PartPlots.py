from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class PartPlots:
    """ A class to represent plot"""
    def __init__(self,label, data_, partido):
        """Constructs all the attributes for kpiplot class"""
        self.label = label
        self.data = pd.DataFrame(data_)
        self.partido = partido
        self.cuenta = self.data.groupby(['Partido']).count()
        self.cuenta = self.cuenta.reset_index()
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

        fig = px.bar(self.cuenta, x="Partido", y="Senadores")
        
        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        layout = html.Div(
            [
             html.Div(self.label,className='kpi-label'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=PartPlots.figura(self)),
            ]
        )
        return layout