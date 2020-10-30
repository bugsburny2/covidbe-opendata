import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

from flask_babel import get_locale, gettext


from graphs import register_plot_for_embedding

df_app = pd.read_csv('static/csv/coronalert.csv')


@register_plot_for_embedding("coronalert-be")
def plot_coronalert():
    idx = pd.date_range(df_app.DATE.min(), df_app.DATE.max())

    df_app.index = pd.DatetimeIndex(df_app.index)
    df_grouped = df_app.groupby(['RISK_LEVEL']).agg({'COUNT': 'sum'})
    print(df_grouped)

    newin_bar = go.Bar(x=idx, y=df_app.COUNT, name=gettext('#New Hospitalized'))
    # df_app.query('RISK_LEVEL<=7')

    # newin_bar = px.bar(x=df_app.index, y=df_app.COUNT)
    fig_coronalert = px.bar(df_app, x="DATE", y="COUNT", color="RISK_LEVEL_LABEL",
                       hover_data=['RISK_LEVEL_LABEL'], barmode='stack')
    fig_coronalert.update_layout(template="plotly_white", height=500, margin=dict(l=0, r=0, t=30, b=0),
                            title=gettext("Temporary Exposure Keys"))
    return fig_coronalert


def plot_coronalert_no_segregation():
    idx = pd.date_range(df_app.DATE.min(), df_app.DATE.max())

    df_app.index = pd.DatetimeIndex(df_app.index)
    df_grouped = df_app.groupby(["DATE"]).agg({"COUNT": 'sum'})
    print(df_grouped)

    fig_hospi = px.bar(df_app, x="DATE", y="COUNT", color="COUNT", )  # barmode = 'stack'
    fig_hospi.update_layout(template="plotly_white", height=500, margin=dict(l=0, r=0, t=30, b=0),
                            title=gettext("Temporary Exposure Keys"))
    return fig_hospi


# plot_coronalert_no_segregation()
# plot_coronalert()