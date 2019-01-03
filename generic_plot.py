#!/usr/bin/env python

import numpy as np
import scipy.stats as stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv
import sys

file = sys.argv[1]
outfile = sys.argv[2]

values = []

# read data
with open(file, 'r') as f:
    reader = csv.reader(f)
    headers = reader.next()
    i = 0
    for h in headers:
        print h, i
        i += 1

    for row in reader:
        val = int(row[1])
        # filter low values for company per person
        values.append(val)

plt.figure(0)

## Uncomment to fit gamma or chi2
# xmin, xmax = 0, max(values)
# lnspc = np.linspace(xmin, xmax, 1000)
# print xmin, xmax, len(values)
#
# params  = stats.gamma.fit(values)
# pdf_gamma = stats.gamma.pdf(lnspc, *params)
# plt.plot(lnspc, pdf_gamma, label="Gamma")
#
# params = stats.chi2.fit(values)
# pdf_chi2 = stats.chi2.pdf(lnspc, *params)
# plt.plot(lnspc, pdf_chi2, label="Chi^2")

## Uncommect to plot with custom site of bins
# plt.hist(values, normed = True, bins=[0,1,2,3,4,5,6,7,8,9,10,12,14,17,20,22,25,27,30,35,40,45,50,60,100])

## Or use even sizes of bins
# binwidth = 100
# plt.hist(values, bins=range(min(values), max(values) + binwidth, binwidth))


# save the plot
plt.savefig(outfile, dpi = 200)
