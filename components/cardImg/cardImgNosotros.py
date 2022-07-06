from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

class cardImgNos:
    """ A class to show a card with image"""
    def __init__(self, name, profesion, descripcion):
        """Constructs all the attributes for kpiplot class"""                                         #Title of graph
        self.name = name                            #Data that is going to graph
        self.path = 'assets\ImgNos\\' + str(name) +'.jpg'
        self.profesion = profesion
        self.descripcion = descripcion
        

    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        cardk = [
                    dbc.CardImg(src=self.path, top=True),
                    dbc.CardBody(
                        [
                            html.H4(self.name, className="card-title"),
                            html.P(self.profesion,className="card-text",),
                            html.P(self.descripcion,className="card-text",),
                        ]
                    ),
                ]

        layout = html.Div(
            [
                dbc.Card(cardk)
            ]
        )
        return layout