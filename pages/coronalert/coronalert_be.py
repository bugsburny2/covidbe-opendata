import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask_babel import get_locale, gettext

from graphs.coronalert import plot_coronalert



def display_coronalert():
    return [
        html.H2(gettext("Coronalert")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='coronalert-be',
                              figure=plot_coronalert(),
                              config=dict(locale=str(get_locale())))),
        ]),


    ]
