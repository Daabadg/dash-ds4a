from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA

class plotModelo:
    """ A class to represent plot"""
    def __init__(self,label, data_, partido):
        """Constructs all the attributes for kpiplot class"""
        self.label = label                                          #Title of graph
        self.data = pd.DataFrame(data_)
        self.partido = partido                        #Data that is going to graph
        #self.partido = partido
        self.cuenta = self.data[self.data.PARTIDO == partido]

        self.cuenta.index = pd.to_datetime(self.cuenta['DATE_PROCESO'], format='%Y-%m-%d')
        self.cuenta = self.cuenta.sort_index()

        vSplitTime = pd.to_datetime("2020-08-01", format='%Y-%m-%d')
        self.train = self.cuenta[self.cuenta.DATE_PROCESO <= vSplitTime]
        self.test  = self.cuenta[self.cuenta.DATE_PROCESO >= vSplitTime]
        self.y = self.train["CASOS_TOTALES"]
       
    
    def getSARIMAXmodel(self):
        ARMAmodel = SARIMAX(self.y, order = (1, 0, 1))
        ARMAmodel = ARMAmodel.fit()
        y_pred = ARMAmodel.get_forecast(len(self.test.index))
        y_pred_df = y_pred.conf_int(alpha = 0.05)
        y_pred_df["Predictions"] = ARMAmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
        y_pred_df.index = self.test.index
        y_pred_out = y_pred_df["Predictions"]
        return y_pred_out, ARMAmodel

    def getARIMAmodel(self):
        ARIMAmodel = ARIMA(self.y, order = (3, 2, 2))
        ARIMAmodel = ARIMAmodel.fit()
        y_pred = ARIMAmodel.get_forecast(len(self.test.index))
        y_pred_df = y_pred.conf_int(alpha = 0.05)
        y_pred_df["Predictions"] = ARIMAmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
        y_pred_df.index = self.test.index
        y_pred_out = y_pred_df["Predictions"] 
        return y_pred_out, ARIMAmodel

    #@staticmethod
    def figura(self):
        #print(self.cuenta)
        #Create figure with specifics

        y_pred_sarimax, model_sarimax = self.getSARIMAXmodel()
        y_pred_arima  , model_arima   = self.getARIMAmodel()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x = y_pred_sarimax.index, y = y_pred_sarimax, mode='lines', name='SARIMAX MODEL'))
        fig.add_trace(go.Scatter(x = y_pred_arima.index, y = y_pred_arima, mode='lines', name='ARIMA MODEL'))
        fig.add_trace(go.Scatter(x = self.train.index, y = self.train["CASOS_TOTALES"], mode='lines', name='TRAIN'))
        fig.add_trace(go.Scatter(x = self.test .index, y = self.test ["CASOS_TOTALES"], mode='lines', name='TEST'))
        fig.update_xaxes(tickangle=45)

        fig.update_layout(
            title='Train/Test split for casos',
            xaxis_title='Date',
            yaxis_title='Conteo de casos',
            legend_title='Datos',
        )

        return fig


    def display(self):
        """Displays the card with label, kpi and a mini-plot from the data"""
        #print(type(self.data))
        
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             #html.H2(self.kpi,className='kpi-number d-flex justify-content-end '),
             dcc.Graph(figure=plotModelo.figura(self),
             config={
                'fillFrame': False,
                'frameMargins':0
             },
             ),
            ]
        )
        return layout