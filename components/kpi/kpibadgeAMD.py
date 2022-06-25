from dash import html 

import dash_bootstrap_components as dbc

class kpibadgeAMD:
    def __init__(self,kpi,label, name):
        self.kpi = kpi
        self.label = label
        self.who = name
        

    def display(self):
        layout = html.Div(
            [
             html.Div(self.label,className='h5'),
             html.H2(self.who,className='h6'),
             html.H2(self.kpi,className='d-flex justify-content-end'),
             #dbc.Badge(self.badgetype, color=self.color, className="mr-1"),
            ], className='card m-4'
        )
        return layout
  