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
JPVP = cardImgNos('Johan Pool Valero Perez', 'Ingeniero de sistemas', 'Data Engineer apassionate by the Big data and the Machine Learning. Vampire hunter in free time. De Santa Marta, Magdalena, Colombia')
DAAG = cardImgNos('Diego Alejandro Abad Gómez', 'Mechanical Engineer', 'llll')
JFMA = cardImgNos('Juan Fernando Montoya Agudelo', 'no dijo', 'llll')
EMJ = cardImgNos('Elquis Manjarrés Jiménez  ', 'Master in Applied Statistics with experience in Metrology.', 'Chemical Engineer with experience in transformation and production through physical, chemical and biochemical processes and services.')


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
               JPVP.display()
            ]),
            dbc.Col([
               DAAG.display()
            ])
            ,dbc.Col([
               JFMA.display()
            ]),
            dbc.Col([
               EMJ
               .display()
            ]),
            dbc.Col([
               JFMA.display()
            ]),
        ]),
    
])


#callbacks

