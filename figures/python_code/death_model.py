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

###############################################################################
### PLOT THE UTILITY SURFACE & TRACE OF DESIGNS
###############################################################################

## IMPORT DATA
util_surf = np.loadtxt('../data/death_model/simpledeath_1d_util.txt')

## PLOT FIGURE 1a
plt.axvline(1.61, 0, 35, color = col[0], linestyle=':')
plt.plot(util_surf[:,0], util_surf[:,1], color = col[3])
plt.xlim(0,10)
plt.ylim(0,35)
plt.xlabel('Design time')
plt.ylabel('Utility')
plt.text(1.8,1,r'$\tau* \approx 1.61$', fontsize=12, color=col[0])
plt.show()

## IMPORT DATA
## Utility has been estimated so still some stochasticity to estimated value
design_traces = np.loadtxt('../data/death_model/simpledeath_traces.txt')

## PLOT FIGURE 1b
plt.figure()
for i in range(11):
    plt.plot(design_traces[i], color = col[i%6+1])
plt.ylim(0,10)
plt.axhline(1.61, 0, 100, color=col[0], linestyle=':')
plt.ylabel('Design time')
plt.xlabel('Utility evaluations')
plt.xticks(np.linspace(0,100, 5), np.linspace(0,100, 5, dtype=np.int32)*100)
plt.text(95,1,r'$\tau^*$', fontsize=16, color = col[0])
plt.show()
