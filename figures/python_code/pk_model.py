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

Scol = col[0]; Acol = col[3]; Mcol = col[6]; Mcol2 = col[5]



###############################################################################
### PLOT COMPARISON OF UTILITY BOXPLOT
###############################################################################

## IMPORT DATA
a = np.loadtxt('../data/pk_model/ace_utils_18m.txt')
s = np.loadtxt('../data/pk_model/sgd_m1_utils_18m.txt')
m1 = np.loadtxt('../data/pk_model/muller_J1_utils_18m.txt')
m2 = np.loadtxt('../data/pk_model/muller_J2_utils_18m.txt')

a_ph2 = np.loadtxt('../data/pk_model/ace_utils_ph2_18m.txt')
s_ph2 = np.loadtxt('../data/pk_model/sgd_utils_ph2_18m.txt')
m1_ph2 = np.loadtxt('../data/pk_model/muller_J1_utils_ph2_18m.txt')
m2_ph2 = np.loadtxt('../data/pk_model/muller_J2_utils_ph2_18m.txt')

init = np.loadtxt('../data/pk_model/init_utils.txt')
unif = np.loadtxt('../data/pk_model/unif_utils.txt')

## PLOT FIGURE 2
plt.figure().set_size_inches(10., 5.)
bp = plt.boxplot([m2_ph2, m1_ph2, s_ph2, a_ph2, m2, m1, s, a, init], vert=False, patch_artist = True)
plt.yticks(np.arange(1,10),['Muller2 + phII','Muller1 + phII', 'SGO-FIG + phII','ACE + phII','Muller2','Muller1','SGO-FIG','ACE','Initial states'])
plt.axvline(np.mean(unif), 0, 5)
plt.xlabel('Expected utility')
plt.xlim(1.5,4.25)
bp_cols = [Mcol2, Mcol, Scol, Acol, Mcol2, Mcol, Scol, Acol, 'lightsteelblue']
for patch, color in zip(bp['boxes'], bp_cols):
    patch.set_facecolor(color)
for element in ['whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
plt.show()


###############################################################################
### PLOT UTILITY TRACES
###############################################################################

### IMPORT DATA
sgd18 = np.loadtxt('../data/pk_model/sgd_m1_trace_18m.txt')
ace18 = np.loadtxt('../data/pk_model/ace_trace_18m.txt')

## PLOT FIGURE 3
x_ace18 = np.linspace(0,18700000, np.shape(ace18)[1])
plt.plot(x_ace18, np.transpose(ace18), color=Acol, alpha=0.2)
plt.ylim(1.5,4)
plt.xlabel(r'Utility evaluations ($\times 10^7)$')
plt.ylabel('Expected utility')
plt.xticks(np.linspace(0,18000000, 7), np.linspace(0,18, 7)/10)
plt.show()

x_sgd18 = np.linspace(0,18700000, np.shape(sgd18)[1])
plt.plot(x_sgd18, np.transpose(sgd18), color=Scol, alpha=0.1)
plt.ylim(1.5,4)
plt.xlabel(r'Utility evaluations ($\times 10^7)$')
plt.ylabel('Expected utility')
plt.xticks(np.linspace(0,18000000, 7), np.linspace(0,18, 7)/10)
plt.show()


###############################################################################
### PLOT OF RETURNED DESIGNS
###############################################################################

## IMPORT DATA
d_a18m = np.loadtxt('../data/pk_model/ace_designs_18m.txt')
d_s18m = np.loadtxt('../data/pk_model/sgd_designs_18m.txt')
d_m18m = np.loadtxt('../data/pk_model/muller_J1_designs_18m.txt')
d2_a18m = np.loadtxt('../data/pk_model/ace_designs_ph2_18m.txt')
d2_s18m = np.loadtxt('../data/pk_model/sgd_designs_ph2_18m.txt')
d2_m18m = np.loadtxt('../data/pk_model/muller_J1_designs_ph2_18m.txt')

x = np.repeat(np.arange(1,16),100).reshape((15,100)).transpose()

fig = plt.figure()
fig.set_size_inches(12., 8.)

## PLOT FIGURE 4a
plt.subplot(2,3,1)
plt.scatter(x, d_s18m, s=100, alpha=0.05, color = Scol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6))
plt.xticks(np.arange(1,16))
plt.ylabel('Time')
plt.title('')#r'$1.87 \times 10^7$', loc = 'left', fontsize=14)
num_at_8_2 = np.sum(d_s18m>8,0)
for i in range(15):
    if(i%2==0):
        plt.text(i+0.7,9.5,num_at_8_2[i], fontsize=8, color=Scol)
    else:
        plt.text(i+0.7,6.2,num_at_8_2[i], fontsize=8, color=Scol)

## PLOT SUBFIGURE 4b
plt.subplot(2,3,2)
plt.scatter(x, d_a18m, s=100, alpha=0.05, color=Acol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6), '')
plt.xticks(np.arange(1,16))
plt.ylabel('')

## PLOT FIGURE 4c
ax2 = plt.subplot(2,3,3)
plt.scatter(x, d_m18m, s=100, alpha=0.05, color=Mcol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6), '')
plt.xticks(np.arange(1,16))
plt.ylabel('')
ax2r = ax2.twinx()
ax2r.get_yaxis().set_ticks([])
ax2r.set_ylabel(r'$1.87 \times 10^7$')

##PLOT SUBPLOT 4d
plt.subplot(2,3,4)
plt.scatter(x, d2_s18m, s=100, alpha=0.05, color = Scol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6))
plt.xticks(np.arange(1,16))
plt.xlabel('Observation index')
plt.ylabel('Time')
plt.title('')#r'$1.87 \times 10^7$', loc = 'left', fontsize=14)
num_at_8_2 = np.sum(d2_s18m>8,0)
for i in range(15):
    if(i%2==0):
        plt.text(i+0.7,9.5,num_at_8_2[i], fontsize=8, color=Scol)
    else:
        plt.text(i+0.7,6.2,num_at_8_2[i], fontsize=8, color=Scol)

##PLOT SUBPLOT 4e
plt.subplot(2,3,5)
plt.scatter(x, d2_a18m, s=100, alpha=0.05, color=Acol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6), '')
plt.xticks(np.arange(1,16))
plt.xlabel('Observation index')
plt.ylabel('')

##PLOT SUBPLOT 4f
ax2 = plt.subplot(2,3,6)
plt.scatter(x, d2_m18m, s=100, alpha=0.05, color=Mcol)
plt.ylim(-1,25)
plt.yticks(np.arange(0,28,6), '')
plt.xticks(np.arange(1,16))
plt.xlabel('Observation index')
plt.ylabel('')
ax2r = ax2.twinx()
ax2r.get_yaxis().set_ticks([])
ax2r.set_ylabel(r'$1.87 \times 10^7$ + ACE phase II')

fig.subplots_adjust(wspace=0, hspace=0)
plt.tight_layout()
plt.show()


###############################################################################
### PLOT OF SGD TRACES FOR VARYING BATCH SIZE USED IN MC ESTIMATE
###############################################################################

## IMPORT DATA

## Only look at the first 100k of sgd using a batch size of 1
## (as only interested in behaviour in this region)
sgd1_first100k = np.loadtxt('../data/pk_model/sgd_m1_trace_first100k.txt')
x_sgd1_first100k = np.linspace(0,100000, np.shape(sgd1_first100k)[1])

sgd1 = np.loadtxt('../data/pk_model/sgd_m1_trace_18m.txt')
sgd10 = np.loadtxt('../data/pk_model/sgd_m10_trace_18m.txt')
sgd100 = np.loadtxt('../data/pk_model/sgd_m100_trace_18m.txt')

x_sgd1 = np.linspace(0, 18700000, np.shape(sgd1)[1])
x_sgd10 = np.linspace(0, 18700000, np.shape(sgd10)[1])
x_sgd100 = np.linspace(0, 18700000, np.shape(sgd100)[1])


## PLOT FIGURE 5

plt.figure().set_size_inches(12,8)

plt.subplot(231)
plt.plot(x_sgd1_first100k, sgd1_first100k.T, color=col[0], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,100000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 100000)
plt.xlabel(r'Iterations $(\times 10^5)$')
plt.ylabel('Expected utility')
plt.title(r'$K=1$', size=12)

plt.subplot(232)
plt.plot(x_sgd10/10, sgd10.T, color=col[3], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,100000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 100000)
plt.xlabel(r'Iterations $(\times 10^5)$')
plt.yticks(np.arange(1.5, 4.1, 0.5), [])
plt.title(r'$K=10$', size=12)

plt.subplot(233)
plt.plot(x_sgd100/100, sgd100.T, color=col[6], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,100000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 100000)
plt.xlabel(r'Iterations $(\times 10^5)$')
plt.yticks(np.arange(1.5, 4.1, 0.5), [])
plt.title(r'$K=100$', size=12)

plt.subplot(234)
plt.plot(x_sgd1, sgd1.T, color=col[0], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,1000000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 1000000)
plt.xlabel(r'Utility evaluations $(\times 10^6)$')
plt.ylabel('Expected utility')

plt.subplot(235)
plt.plot(x_sgd10, sgd10.T, color=col[3], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,1000000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 1000000)
plt.xlabel(r'Utility evaluations $(\times 10^6)$')
plt.yticks(np.arange(1.5, 4.1, 0.5), [])

plt.subplot(236)
plt.plot(x_sgd100, sgd100.T, color=col[6], alpha=0.2)
plt.ylim(1.5,4)
plt.xticks(np.linspace(0,1000000, 5), np.linspace(0,10, 5)/10)
plt.xlim(0, 1000000)
plt.xlabel(r'Utility evaluations $(\times 10^6)$')
plt.yticks(np.arange(1.5, 4.1, 0.5), [])
plt.show()

