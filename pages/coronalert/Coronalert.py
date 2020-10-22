#!/usr/bin/env python
# coding: utf-8
#@author: ggrosjean
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from flask_babel import gettext
from plotly.subplots import make_subplots

from graphs import register_plot_for_embedding

df_app = pd.read_csv('static/csv/coronalert.csv')

def compute_coronalert():
    x=1

def plot_coronalert():
    idx = pd.date_range(df_app.DATE.min(), df_app.DATE.max())
   
    df_app.index = pd.DatetimeIndex(df_app.index)
    df_grouped = df_app.groupby(['RISK_LEVEL']).agg({'COUNT': 'sum'})
    print (df_grouped)
        
    newin_bar = go.Bar(x=idx, y=df_app.COUNT, name=gettext('#New Hospitalized'))
   
    
    #newin_bar = px.bar(x=df_app.index, y=df_app.COUNT)
    fig_hospi = px.bar(df_app, x="DATE", y="COUNT", color="RISK_LEVEL", 
            hover_data=['RISK_LEVEL'], barmode = 'stack') 
    fig_hospi.update_layout(template="plotly_white", height=500, margin=dict(l=0, r=0, t=30, b=0),
                           title=gettext("Temporary Exposure Keys"))
    return fig_hospi

compute_coronalert()
plot_coronalert()