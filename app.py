#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc

from callbacks import register_callbacks

# Dash instance declaration
app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.MINTY], update_title='Cargando...'
)
app.config.suppress_callback_exceptions=True


#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple(
    [
    
    dbc.NavItem(dbc.NavLink("Inicio", href="/")),
    dbc.NavItem(dbc.NavLink( "Nosotros", href="/nosotros")),
    #dbc.NavItem(dbc.NavLink("Partido", href="/partido"))
    ],

    brand="Transparencia Colombia",
    color="primary",
    dark=True,
    className="text-center mb-2",
)


button_group = dbc.ButtonGroup(
    [
        dbc.Button([
                    'Senador'
                ],id="btt_senador",  href="/senador"),
        dbc.Button([
                    'Partido'
                ],id="btt_partido",  href="/partido"),
        dbc.Button([
                    'Comparar'
                ],id="btt_comparar",  href="/comparacion"),
    ],
    vertical=True,
)

#Main layout
app.layout = dbc.Container(

    [
        navbar,
        dbc.Row([
            dbc.Col([
                button_group
            ], md=1, lg=1),  
            dbc.Col([
                dl.plugins.page_container,
            ], md=11, lg=11),
        ]),
    

        
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
register_callbacks(app)

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)