#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## SET WORKING DIRECTORY TO SOURCE FILE LOCATION
import os
import inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.stack()[0][1])))

## IMPORT RELEVANT MODULES
import numpy as np
import matplotlib.pyplot as plt
col = plt.rcParams['axes.prop_cycle'].by_key()['color']

Scol = col[0]; Acol = col[3]

###############################################################################
### PLOT BOXPLOT COMPARING SGD TO ACE
###############################################################################

## IMPORT DATA
tr_sgd = np.loadtxt('../data/geo_model/sgd_traces.txt')
tr_ace = np.loadtxt('../data/geo_model/ace_traces.txt')

## PLOT FIGURE 7a
plt.figure().set_size_inches(5., 5.)
bp = plt.boxplot([tr_sgd[:,-1], tr_ace[:,-1]], patch_artist = True)
plt.xticks(np.arange(1,3), ['SGO-FIG', 'ACE'])
plt.ylabel('Utility')
bp_cols = [Scol, Acol]
for patch, color in zip(bp['boxes'], bp_cols):
    patch.set_facecolor(color)
for element in ['whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp[element], color='black')
plt.show()


###############################################################################
### PLOT TRACE PLOTS
###############################################################################

x_sgd = np.linspace(0,50000, np.size(tr_sgd[0]))
x_ace = np.linspace(0,85000, np.size(tr_ace[0]))

plt.axhline(20.37012, color = col[5])
plt.plot(x_sgd, np.transpose(tr_sgd), color=Scol, alpha = 0.05)
plt.plot(x_ace, np.transpose(tr_ace), color=Acol, alpha = 0.05)
plt.ylabel('Utility')
plt.xlabel('Utility evaluations')
from matplotlib.lines import Line2D
plt.legend([Line2D([0],[0], color = Scol), Line2D([0],[0], color = Acol), Line2D([0],[0], color = col[5])], 
            ['SGO-FIG', 'ACE', 'Uniform'])
plt.show()


###############################################################################
### PLOT DESIGNS FOR DIFFERENT CHOICES OF ELL AND GAMMA
###############################################################################

## GET DATA FILES
files = os.listdir('../data/geo_model/change_l_gamma')

for i in range(np.size(files)):
    ## LOAD DATA
    x = np.loadtxt('../data/geo_model/change_l_gamma/'+str(files[i]))
    ## PLOTS USED IN FIGURE 6
    plt.scatter(x[:,0], x[:,1])
    plt.xticks([])
    plt.yticks([])
    plt.xlim(-0.55,0.55)
    plt.ylim(-0.55,0.55)
    plt.show()
