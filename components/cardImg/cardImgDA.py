from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class cardImgPartido:
    """ A class to show a card with image"""
    def __init__(self,label, partido):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        #self.name = name                            #Data that is going to graph
        self.path = 'assets\ImgDA\\' + str(partido) +'.jpg'
        self.partido = partido
        #self.descripcion = descripcion
        

    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        cardk = [
                    dbc.CardImg(src=self.path, top=True),
                    dbc.CardBody(
                        [
                            html.H6(self.partido, className="card-title"),
                            #html.P(self.partido,className="card-text",),
                            #html.P(self.descripcion,className="card-text",),
                        ]
                    ),
                ]

        layout = html.Div(
            [
                dbc.Card(cardk)
            ]
        )
        return layout