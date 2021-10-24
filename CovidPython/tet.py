# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
colours = [100,95,90,85,80]
df = pd.read_csv('D:\Desktop\Book1.csv')

fig =px.area(df, color='floor', x='timestamp', y='value', title='Time Series with Rangeslider')

fig.update_layout(
    yaxis_range = [70,100]
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    

    dcc.Graph(
        id='example-graph',
        figure=fig
    )


])
# style_data_conditional=[
#         { 
#             'if': {
#                 'filter_query': '{value}' > 90,
#                 'column_id': 'value'
#             },
#             'color': 'red'
#         }

if __name__ == '__main__':
    app.run_server(debug=True)