import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/nosotros")

from dash import  dcc, html, Input, Output, callback, State
import plotly.express as px
import pandas as pd

from components.cardImg.cardImgNosotros import cardImgNos

#Llamado de components
#cardSen = cardImg("AIDA MARINA QUILCUE VIVAS", "AIDA MARINA QUILCUE VIVAS")

AMD = cardImgNos('Andrea Martinez Diaz', 'Ingeniera mecatrónica', 'Ingeniera mecatrónica con conocimiento e interés en control inteligente, inteligencia artificial y análisis de datos. Amante del baloncesto y las series.','http://www.linkedin.com/in/anmartinezdi')
JPVP = cardImgNos('Johan Pool Valero Perez', 'Ingeniero de sistemas', 'Ingeniero de datos apasionado por el Big data y el Machine Learning. Cazador de vampiros en el tiempo libre. De Santa Marta, Magdalena, Colombia','https://www.linkedin.com/in/johan-v/')
DAAG = cardImgNos('Diego Alejandro Abad Gómez', 'Ingeniero mecánico', 'Ingeniero mecánico aprendiendo paso a paso acerca del mundo de la tecnología e inteligencia artificial. En el tiempo libre le gusta hacer muchas cosas como dormir y comer.','https://www.linkedin.com/in/daabadg/')
JFMA = cardImgNos('Juan Fernando Montoya Agudelo', 'Ingeniero mecatrónico', 'Estudiante de octavo semestre de Ingeniería Mecatrónica, autodidacta, con conocimientos básicos de programación en Java, SQL, electrónica y con una gran disposición de seguir aprendiendo.','https://www.linkedin.com/in/juan-fernando-montoya-agudelo-7b1618200/')
EMJ = cardImgNos('Elquis Manjarrés Jiménez', 'Maestría en estadística aplicada con experiencia en metrología', 'Ingeniero químico con experiencia en transformación y producción a través de procesos físicos, químicos y bioquímicos y servicios.','https://www.linkedin.com/in/elquis-manjarres-jimenez/')
JAGC = cardImgNos('Julián Andrés Gutiérrez Castaño', 'Ingeniero industrial', 'Ingeniero industrial con experiencia en creación y aplicación de metodologías constructivistas, gestión de la producción e investigación de operaciones.','https://www.linkedin.com/in/julian-gutierrez-c')



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
               EMJ.display()
            ]),
            dbc.Col([
               JAGC.display()
            ]),
        ]),
    
])


#callbacks

