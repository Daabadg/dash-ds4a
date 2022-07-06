from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class piechartSen:
    """ A class to represent plot"""
    def __init__(self,label, data_, senador):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        self.data = pd.DataFrame(data_)                             #Data that is going to graph

        datadf1 = [[senador,'Procesos publicos',self.data.iloc[0]['CANTIDAD_PROCESOS_PUBLICOS']],[senador,'Procesos privados',self.data.iloc[0]['CANTIDAD_PROCESOS_PRIVADOS']]]
        columnsdf1 = ['senador','tipo','casos']
        self.cuenta = pd.DataFrame(datadf1,columns = columnsdf1)

        
    #@staticmethod
    def figura(self):

        #Create figure with specifics
        fig = px.pie(self.cuenta, names=self.cuenta['tipo'], values=self.cuenta['casos'],color_discrete_sequence=px.colors.qualitative.Set2,)
        fig.update_layout(
            autosize=True,
            width=250,
            height=250,
            margin=dict(
                l=20,
                r=20,
                b=20,
                t=20,
                pad=3
            ),
            legend=dict(
                yanchor="top",
                y=1,
                xanchor="left",
                x=0.01
        )
        )


        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             dcc.Graph(figure=piechartSen.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ], className='card'
        )
        return layout