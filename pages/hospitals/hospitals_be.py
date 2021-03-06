import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask_babel import get_locale, gettext

from graphs.hopitals import bar_hospitalization, \
    hospi_over_death_smooth,\
    hospi_smooth,death_smooth,\
    icu_over_hospi,newin_smooth,\
    death_over_icu_smooth, \
    bar_hospitalization_ICU, \
    bar_hospitalization_tot, \
    bar_hospitalization_in_out,\
    exp_fit_hospi,hospi_waves
from pages.sources import display_source_providers, source_sciensano


def display_hospitals():
    return [
        html.H2(gettext("Total Hospitalizations")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=bar_hospitalization_tot(),
                              config=dict(locale=str(get_locale())))),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=exp_fit_hospi(),
                              config=dict(locale=str(get_locale())))),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=hospi_waves(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Total ICU Hospitalizations")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=bar_hospitalization_ICU(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Daily IN-OUT Hospitalizations")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=bar_hospitalization_in_out(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Total Hospitalizations Avg over 7 past days")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=hospi_smooth(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("New daily hospitalizations Avg over 7 past days")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=newin_smooth(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Total Deaths Avg over 7 past days")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=death_smooth(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Total ICU/ Total Hospitalization")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=icu_over_hospi(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Deaths/ Total ICU (Avg over 7 past days)")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=death_over_icu_smooth(),
                              config=dict(locale=str(get_locale())))),
        ]),
        html.H2(gettext("Deaths/ Total Hospitalization (Avg over 7 past days)")),
        dbc.Row([
            dbc.Col(dcc.Graph(id='hospitalization-be',
                              figure=hospi_over_death_smooth(),
                              config=dict(locale=str(get_locale())))),
        ]),

        display_source_providers(source_sciensano)
    ]
