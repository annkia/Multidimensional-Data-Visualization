# - *- coding: utf- 8 - *-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
df = pd.read_csv('iris2.csv')
features = ['długość działki kielicha','szerokość działki kielicha','długość płatka korony','szerokość płatka korony]


app.layout = html.Div([
        html.H1('Porównanie wymiarów irysa'),
        html.Div([
            dcc.Dropdown(
                id='xaxis_drop',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='szerokość płatka korony'

            )
        ],
        style={'width': '33.3%', 'display': 'inline-block', 'font-family': 'Verdana'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis_drop',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='szerokość działki kielicha'

            )
        ],
        style={'width': '33.3%', 'display': 'inline-block', 'font-family': 'Verdana'}),
        html.Div([
            dcc.Dropdown(
                id='zaxis_drop',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='petal width'
            )
        ],
        style={'width': '33.3%', 'display': 'inline-block', 'font-family': 'Verdana'}),

            dcc.Graph(id='scatter',
                    style=dict(width='1200px',
                                height='600px')
                    )

        ])

@app.callback(
    Output('scatter', 'figure'),
    [Input('xaxis_drop', 'value'),
     Input('yaxis_drop', 'value'),
      Input('zaxis_drop', 'value')])
def update_graph(xaxis_name, yaxis_name, zaxis_name):
    return {
        'data': [go.Scatter3d(
            x=df[xaxis_name],
            y=df[yaxis_name],
            z=df[zaxis_name],
            text=df['Species'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.7,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
        scene=dict(
                xaxis={'title': xaxis_name.title()+' [cm]'},
                yaxis={'title':yaxis_name.title() +' [cm]'},
                zaxis={'title':zaxis_name.title()+' [cm]'}
            )

        )
    }

if __name__=='__main__':
    app.run_server()
