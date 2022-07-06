from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class plotTwoxTwo:
    """ A class to represent plot"""
    def __init__(self,label, data_,senador1,senador2,x,y,color):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        self.data = data_                                          #Data that is going to graph
        #self.partido = partido
        #self.cuenta = self.data.groupby([str(col_gr1),str(col_gr2)]).count()      #Group by and filtter applied
        #self.cuenta = self.cuenta.reset_index()  
        self.cuenta = pd.DataFrame(self.data)                   
        self.cuenta = self.cuenta.query("PERSON_NAME == '"+str(senador1)+ "' | PERSON_NAME == '"+ str(senador2)+"'")
        self.x = x                                                  #column of data that its going to be x-axis of graph
        self.y = y
        #self.y2 = y2
        self.color = color
        #self.cuenta_partido = self.data.groupby(partido,["Genero"]).count()
    
    #@staticmethod
    def figura(self):

        #print(self.cuenta)
        #Create figure with specifics
        #print(self.cuenta)

        fig = px.bar(self.cuenta, x=str(self.x), y=str(self.y),barmode='group',color_discrete_sequence=px.colors.qualitative.Set2,color=self.color)
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
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=plotTwoxTwo.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ]
        )
        return layout