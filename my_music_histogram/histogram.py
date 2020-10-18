#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

START_YEAR = 1957
END_YEAR = 2014
NO_YEARS = END_YEAR - START_YEAR + 1

x_years = np.linspace(START_YEAR, END_YEAR, NO_YEARS)
y_score = np.zeros(NO_YEARS)

infile = open('years.txt', 'r')
all_lines = infile.readlines()

for year_entry in all_lines:
    y_score[int(year_entry) - START_YEAR] += 1

plt.plot(x_years, y_score)
plt.show()

