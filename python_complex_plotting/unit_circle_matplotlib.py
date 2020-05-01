#!/usr/bin/python3

from matplotlib import pyplot, numpy
from math import pi, e

SAMPLES_N = 80
ARG_MAX = 2 * pi

arguments = list(numpy.linspace(0, ARG_MAX, SAMPLES_N + 1))

y = []
for x in arguments:
    y.append(e ** (1j * x))
y = numpy.array(y)

# Flat unit circle plot
figure = pyplot.figure()
ax = figure.add_subplot(121, xlabel="Re", ylabel="Im", title="Unit circle")
ax.scatter(y.real, y.imag, numpy.linspace(0, ARG_MAX, SAMPLES_N + 1) * 3)
ax.grid(True)

# 3D helix plot
ax2 = figure.add_subplot(122, projection='3d', xlabel="Re", ylabel="θ", zlabel="Im", title="Complex exponential")
ax2.plot(y.real, arguments, y.imag)

pyplot.show()
