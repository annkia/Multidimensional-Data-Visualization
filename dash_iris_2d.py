# - *- coding: utf- 8 - *-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

df = pd.read_csv('iris2.csv')
features = ['długość działki kielicha','szerokość działki kielicha','długość płatka korony','szerokość płatka korony']

app.layout = html.Div([
        html.H1('Porównanie wymiarów irysa'),
        html.Div([
            dcc.Dropdown(
                id='xaxis',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='szerokość płatka korony'
            )
        ],
        style={'width': '48%', 'display': 'inline-block', 'font-family': 'Verdana'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis',
                options=[{'label': i.title(), 'value': i} for i in features],
                value='szerokość działki kielicha'
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block', 'font-family': 'Verdana'}),

    dcc.Graph(id='feature-graphic')
], style={'padding':10})




@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    traces=[]
    traces.append(go.Scatter(
        x=df[xaxis_name],
        y=df[yaxis_name],
        text=df['Species'],
        mode='markers',
        marker={
            'size': 15,
            'opacity': 0.5,
            'line': {'width': 0.5, 'color': 'white'}
        }
    )
    )

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title() +' [cm]'},
            yaxis={'title': yaxis_name.title() +' [cm]'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()
