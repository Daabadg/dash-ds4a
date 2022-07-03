from dash import html 

import dash_bootstrap_components as dbc

class kpibadgeAMDsencilla:
    def __init__(self,kpi,label):
        self.kpi = kpi
        self.label = label

        

    def display(self):
        layout = html.Div(
            [
             html.Div(self.label,className='h6'),
             html.H2(self.kpi,className='d-flex justify-content-end'),
             #dbc.Badge(self.badgetype, color=self.color, className="mr-1"),
            ], className='card m-3'
        )
        return layout
  