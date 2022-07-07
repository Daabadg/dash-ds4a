from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class edadHist:
    """ A class to represent plot"""
    def __init__(self, data, partido:str):
        """Constructs all the attributes for kpiplot class"""
        self.data = data
        self.data = data.dropna()
        self.partido = partido
        #self.y = y

        #self.cuenta = self.data.groupby(['Partido']).count()
        #self.cuenta = self.cuenta.reset_index()
        #self.cuenta_partido = self.data.groupby(partido,["Genero"]).count()
    
    #@staticmethod
    def figura(self):
    
        layout = dict(
            autosize=True,
            margin=dict(l=1, r=0, t=0, b=0, pad=0),
            #height=120,
            plot_bgcolor='rgba(0,0,0,0)',
            #yaxis_visible=False,
            yaxis_showticklabels=False,
            xaxis=dict(
                title='',
            ),
        )
       
        cuenta = self.data[self.data['Partido'] == self.partido]['Edad']
        fig = px.histogram(cuenta,x='Edad',nbins=15,text_auto=True)
        fig.update_layout(bargap = 0.1)
    
        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        layout = html.Div(
            [
             html.H4(['Edades']),
             #html.Div(self.label,className='bar-plot'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=edadHist.figura(self)),
            ],#className='card'
        )
        return layout