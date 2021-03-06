# -*- coding: utf-8 -*-
"""LIF and ELIF Complex Models


Leaky Integrate-and-Fire Full Model [ Linear , nonLinear , Threshold , Reset Model & ... ] 

*by : Mostafa Abdollahi*

github.com/m-abdollahi



---

> > > ># ***Linear Exponential Leaky Integrate-and-Fire (LIF) Model ( Ordinary Model)***

# 1 ) Ordinary Model ( without threshold or reset and Start Point)

*   Importing Libraries and Modules
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

pip install brian2

from brian2 import *

"""
*   Set the Neuron
"""

v_rest = -65 * mV        # Rest Potential 
RI = 90 * mV             # RI = I * R = membrane resistance x constant input current = I/G
tau = 10*ms              # Tau = Memberane time Constant

"""
*   Set the LIF differential equations
"""

eqs = '''
dv/dt = (v_rest - v + RI)/tau : volt
'''

"""
*   Set the Neuron Circuit
"""

Methods = 'exact'        # set the method for the equations ( exact or euler)
Run_Time0 = 100*ms      # Import the Run time for Record

G = NeuronGroup(1, eqs, method=Methods)
M = StateMonitor(G, 'v', record=0)
run(Run_Time0)
plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v');

"""# 2 ) Ordinary Model ( with threshold & reset Potential and Start Point)

*   Importing Libraries and Modules
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

pip install brian2

from brian2 import *

"""
*   Set the Neuron
"""

v_rest = -65 * mV                          # Rest Potential 
v_threshold = 'v > 0*mV'                   # Threshold Potential
v_reset = 'v = -40*mV'                     # Reset Potential
v_initial = -70*mV                         # Initail Poteiial Value
RI = 90 * mV                               # RI = I * R = membrane resistance x constant input current = I/G
tau = 10*ms                                # Tau = Memberane time Constant

"""
*   Set the LIF differential equations
"""

eqs = '''
dv/dt = (v_rest - v + RI)/tau : volt
'''

"""
*   Set the Neuron Circuit
"""

Methods = 'exact'        # set the method for the equations ( exact or euler)
Run_Time0 = 100*ms      # Import the Run time for Record

G = NeuronGroup(1, eqs, method=Methods , threshold=v_threshold , reset=v_reset)
M = StateMonitor(G, 'v', record=0)
G.v = v_initial # initial value
run(Run_Time0)
plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v');

"""# 3 ) Ordinary Model plus Refractoriness type Forced Voltage Clamp

*   Importing Libraries and Modules
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

pip install brian2

from brian2 import *

"""
*   Set the Neuron
"""

v_rest = -65 * mV                          # Rest Potential 
v_threshold = 'v > 0*mV'                   # Threshold Potential
v_reset = 'v = -40*mV'                     # Reset Potential
v_initial = -70*mV                         # Initail Poteiial Value
RI = 90 * mV                               # RI = I * R = membrane resistance x constant input current = I/G
tau = 10*ms                                # Tau = Memberane time Constant 
refactorytime = 5*ms                       # Refactory time

"""
*   Set the LIF differential equations
"""

eqs = '''
dv/dt = (v_rest - v + RI)/tau : volt (unless refractory)
'''

"""
*   Set the Neuron Circuit
"""

Methods = 'euler'        # set the method for the equations ( exact or euler)
Run_Time0 = 100*ms      # Import the Run time for Record

G = NeuronGroup(1, eqs, method=Methods , threshold=v_threshold , reset=v_reset,refractory=refactorytime,)
M = StateMonitor(G, 'v', record=0)
G.v = v_initial # initial value
run(Run_Time0)
plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v');

"""# 4 ) Ordinary Model plus Refractoriness type Raised Threshold

*   Importing Libraries and Modules
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

pip install brian2

from brian2 import *

"""
*   Set the Neuron
"""



v_rest = -65 * mV                          # Rest Potential 
vth = 0*mV                                 #first Treshold Potential
vtau = 2*ms                                # Treshold Time Constant
Run_Time0 = 100*ms                         # Run time for Record  
vtheqs = 0 + mt.exp(-Run_Time0/vtau)       # The exponential for The Treshold
v_threshold = 'v > vtheqs*mV'              # Threshold Potential
v_reset = 'v = -40*mV'                     # Reset Potential
v_initial = -70*mV                         # Initail Poteiial Value
RI = 90 * mV                               # RI = I * R = membrane resistance x constant input current = I/G
tau = 10*ms                                # Tau = Memberane time Constant

"""
*   Set the LIF differential equations
"""

eqs = '''
dv/dt = (v_rest - v + RI)/tau : volt 
'''

"""
*   Set the Neuron Circuit
"""

Methods = 'euler'        # set the method for the equations ( exact or euler)
Run_Time0 = 100*ms      # Import the Run time for Record

G = NeuronGroup(1, eqs, method=Methods , threshold=v_threshold , reset=v_reset,)
M = StateMonitor(G, 'v', record=0)
G.v = v_initial # initial value
run(Run_Time0)
plot(M.t/ms, M.v[0])
xlabel('Time (ms)')
ylabel('v');

"""> > > ># ***Exponential Exponential Leaky Integrate-and-Fire (ELIF) Model***

# 1 ) Exponential Model ( with threshold or reset and Start Point)

*   Importing Libraries and Modules
"""

pip install brian2
pip install neurodynex

import brian2 as b2
import matplotlib.pyplot as plt
import numpy as np
from neurodynex.leaky_integrate_and_fire import LIF
from neurodynex.tools import input_factory, plot_tools

"""
*   Set the Neuron
"""

V_REST = -70*b2.mV                           # Reset Potential  
V_RESET = -60*b2.mV                          # Reset Potential
FIRING_THRESHOLD = -50*b2.mV                 # Treshold Potential
MEMBRANE_RESISTANCE = 10. * b2.Mohm          # Membereane R 
MEMBRANE_TIME_SCALE = 8. * b2.ms             # Time Constant
ABSOLUTE_REFRACTORY_PERIOD = 2.0 * b2.ms     # Refactory time
LIF.getting_started()
LIF.print_default_parameters()


