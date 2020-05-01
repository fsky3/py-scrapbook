#!/usr/bin/python3

#Exercise 1.4 in Owen's "Practical Signal Processing"

from matplotlib import pyplot, numpy, colors
from math import pi, e, radians

#Unit circle
SAMPLES_N = 160
ARG_MAX = 2*pi
t = list(numpy.linspace(0, ARG_MAX, SAMPLES_N + 1))
y = list(map(lambda x: e**(1j*x), t))
y = numpy.array(y)

#Handles and labels for the legend
labels = [r'$e^{j\theta}$', 'Series A', 'Series B', 'Series C']
handles = []

#Plot circle
FIG_SIZE = 8 # Side of a square
fig, ax = pyplot.subplots(figsize=(FIG_SIZE, FIG_SIZE))
handles += ax.plot(y.real, y.imag)
ax.set(xlabel="Re", ylabel="Im", title="Unit circle")

#Series of measurement data
data = [[12, 15, 13, 9, 16],
        [358, 1, 359, 355, 2],
        [210, 290, 10, 90, 170]]

#Let measurements 'degrade'
weights = [5, 4, 3, 2, 1]

#Averaging results
results = []
for series in data:
    average_angle = 0 + 0j
    weight_index = 0
    for angle in series:
        exp = weights[weight_index] * e**(1j*radians(angle))
        average_angle += exp
        weight_index += 1
    results.append((average_angle/sum(weights)))

#Normalize for unit length (looks nice, but we loose information)
results = list(map(lambda x: x/abs(x), results))

#Add arrow to graph for each averaged series
color_list = list(colors.BASE_COLORS.keys())
for i in range(len(results)):
    handles += [pyplot.arrow(0, 0, results[i].real, results[i].imag,
                             fc=color_list[i],
                             head_width=0.05,
                             length_includes_head=True)]

#Show the figure
ax.legend(handles, labels)
ax.grid(True)
pyplot.show()
