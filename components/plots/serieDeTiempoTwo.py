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
        self.data['fecha_Mes'] = pd.to_datetime(self.data[str(fecha)]).dt.to_period(freq = 'M')
        self.cuenta = self.data.groupby(['fecha_Mes','PERSON_NAME']).count() 
        self.cuenta.reset_index(inplace = True)
        self.cuenta['fecha_Mes'] = self.cuenta['fecha_Mes'].astype(str)

        self.color = color
    
 
    #@staticmethod
    def figura(self):
        
        #Create figure with specifics
        fig = px.line(self.cuenta, x=self.cuenta['fecha_Mes'], y='ID_PROCESO',color_discrete_sequence=px.colors.qualitative.Set2,color=self.color)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=1,
            xanchor="right",
            x=1
        ))

        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             dcc.Graph(figure=serieDeTiempoTwo.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ]
        )
        return layout