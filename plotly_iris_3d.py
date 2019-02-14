# - *- coding: utf- 8 - *-

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
#from plotly import tools

df = pd.read_csv('iris.csv')

trace_1=go.Scatter3d(
    x = df[df.Species=='setosa']['sepal_length'],
    y = df[df.Species=='setosa']['sepal_width'],
    z = df[df.Species=='setosa']['petal_length'],
    mode = 'markers',
    marker = dict(
        size = 8,
        symbol = 'circle'
    ),
    name = 'Setosa'
    )
trace_2=go.Scatter3d(
    x = df[df.Species=='versicolor']['sepal_length'],
    y = df[df.Species=='versicolor']['sepal_width'],
    z = df[df.Species=='versicolor']['petal_length'],
    mode='markers',
    marker = dict(
            size = 8,
            symbol = 'circle'
        ),
    name = 'Versicolor'
)
trace_3=go.Scatter3d(
    x = df[df.Species=='virginica']['sepal_length'],
    y = df[df.Species=='virginica']['sepal_width'],
    z = df[df.Species=='virginica']['petal_length'],
     mode='markers',
     marker = dict(
           size = 8,
           symbol = 'circle'
       ),
    name = 'Virginica'
)

layout = go.Layout(
    showlegend=True,
    title='Stosunek długości działki kielicha do szerokości działki kielicha <br> i długości płatka korony różnych odmian irysa',
     scene=dict(
         xaxis = dict(title = 'Długość działki kielicha [cm]'), # x-axis label
         yaxis = dict(title = 'Szerokość działki kielicha [cm]'),        # y-axis label
         zaxis = dict(title = 'Długość płatka korony [cm]')
     ),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=70
    )
)
data=[trace_1, trace_2, trace_3]

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='3d-scatter.html')
