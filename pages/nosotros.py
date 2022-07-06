import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/nosotros")

from dash import  dcc, html, Input, Output, callback, State
import plotly.express as px
import pandas as pd

from components.cardImg.cardImgNosotros import cardImgNos

#Llamado de components
#cardSen = cardImg("AIDA MARINA QUILCUE VIVAS", "AIDA MARINA QUILCUE VIVAS")

AMD = cardImgNos('Andrea Martinez Diaz', 'Ingeniera Mecatronica', 'llll')

layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1("Nosotros", className='title ml-2')
            ])
        ]),
         dbc.Row([
            dbc.Col([
               AMD.display()
            ]),
            dbc.Col([
               AMD.display()
            ]),
            dbc.Col([
               AMD.display()
            ])
            ,dbc.Col([
               AMD.display()
            ]),
            dbc.Col([
               AMD.display()
            ]),
        ]),
    
])


#callbacks

