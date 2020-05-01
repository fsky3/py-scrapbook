#!/usr/bin/python3

import numpy
import plotly.graph_objs as go
from math import pi, e

SAMPLES_N = 80
ARG_MAX = 2 * pi

arguments = numpy.linspace(0, ARG_MAX, SAMPLES_N + 1)

y = list(map(lambda x: e ** (1j * x), arguments))
y = numpy.array(y)

# Plot
marker = go.scatter3d.Marker(
         color = 'red',
         size = [x * 25 for x in arguments],
         sizemode = 'area',
         sizemin = 5)

trace = go.Scatter3d(
        x = arguments,
        y = y.real,
        z = y.imag,
        name = '$e^{jt}$',
        mode = 'markers',
        marker = marker)

zero = go.Scatter3d(
       x = arguments,
       y = numpy.zeros(SAMPLES_N),
       z = numpy.zeros(SAMPLES_N),
       name = '$0 + 0j$',
       mode = 'lines',
       line = dict(color = 'gray'))

data = [trace, zero]

scene = dict(
        aspectmode = 'cube',
        xaxis = dict(title = 'θ'),
        yaxis = dict(title = 'Re'),
        zaxis = dict(title = 'Im'))

layout = go.Layout(
         title = 'Unit circle',
         scene = scene,
         showlegend = True)

figure = go.Figure(data = data, layout = layout)

figure.write_html(file = 'figure.html',
                  include_mathjax = 'MathJax-2.7.3/MathJax.js')
