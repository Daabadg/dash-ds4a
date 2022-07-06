from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class plotGrouptwo:
    """ A class to represent plot"""
    def __init__(self,label, data_, col_gr1, col_gr2,x,y):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        self.data = pd.DataFrame(data_)                             #Data that is going to graph
        #self.partido = partido
        #self.cuenta = self.data.groupby([str(col_gr1),str(col_gr2)]).count()      #Group by and filtter applied
        #self.cuenta = self.cuenta.reset_index()  
        self.cuenta = self.data                   
        self.x = x                                                  #column of data that its going to be x-axis of graph
        self.y = y
        self.color = col_gr2                                                  #column of data that its going to be y-axis of graph
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
        #print(self.cuenta)
        fig = px.bar(self.cuenta, x=str(self.x), y=str(self.y),color=self.color,barmode='group',color_discrete_sequence=px.colors.qualitative.Set2,)
        #datadict = [dict(x=self.cuenta,type='bar')]
        
        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=plotGrouptwo.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ]
        )
        return layout