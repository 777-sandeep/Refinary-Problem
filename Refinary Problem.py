#!/usr/bin/env python
# coding: utf-8

# In[177]:


import pandas_ods_reader as pd
import pandas as p
import pulp
from pulp import *
import math
import numpy


# In[178]:


# Defining Sense of Model
model = LpProblem(name = "Refinary_Problem" , sense = LpMaximize)


# In[179]:


Products = ['PP','RP','JO','FO','LO']
Profit = [7,6,4,3.5,1.5]
Availability = [20000,30000]
# Variables
y_vars  = {(i): LpVariable(cat=LpInteger, lowBound=0, name="y_{0}".format(i)) for i in range(len(Products))}
y_vars


# In[180]:


Crude = ['C1','C2']
x_vars  = {(i): LpVariable(cat=LpInteger, lowBound=0, name="x_{0}".format(i)) for i in range(len(Crude))}
x_vars


# In[181]:


NL = LpVariable("NL", lowBound = 0, upBound = None, cat='Continuous')
NM = LpVariable("NM", lowBound = 0, upBound = None, cat='Continuous')
NH = LpVariable("NH", lowBound = 0, upBound = None, cat='Continuous')
OL = LpVariable("OL", lowBound = 0, upBound = None, cat='Continuous')
OH = LpVariable("OH", lowBound = 0, upBound = None, cat='Continuous')
R = LpVariable("R", lowBound = 0, upBound = None, cat='Continuous')

RNL = LpVariable("RNL", lowBound = 0, upBound = None, cat='Continuous')
RNM = LpVariable("RNM", lowBound = 0, upBound = None, cat='Continuous')
RNH = LpVariable("RNH", lowBound = 0, upBound = None, cat='Continuous')
RG = LpVariable("RG", lowBound = 0, upBound = None, cat='Continuous')
CO = LpVariable("CO", lowBound = 0, upBound = None, cat='Continuous')
CG = LpVariable("CG", lowBound = 0, upBound = None, cat='Continuous')

COL = LpVariable("COL", lowBound = 0, upBound = None, cat='Continuous')
COH = LpVariable("COH", lowBound = 0, upBound = None, cat='Continuous')

HNRP = LpVariable("HNRP", lowBound = 0, upBound = None, cat='Continuous')
MNRP = LpVariable("MNRP", lowBound = 0, upBound = None, cat='Continuous')
LNRP = LpVariable("LNRP", lowBound = 0, upBound = None, cat='Continuous')
RGRP = LpVariable("RGRP", lowBound = 0, upBound = None, cat='Continuous')
CGRP = LpVariable("CGRP", lowBound = 0, upBound = None, cat='Continuous')

HNPP = LpVariable("HNPP", lowBound = 0, upBound = None, cat='Continuous')
MNPP = LpVariable("MNPP", lowBound = 0, upBound = None, cat='Continuous')
LNPP = LpVariable("LNPP", lowBound = 0, upBound = None, cat='Continuous')
RGPP = LpVariable("RGPP", lowBound = 0, upBound = None, cat='Continuous')
CGPP = LpVariable("CGPP", lowBound = 0, upBound = None, cat='Continuous')

OLJ = LpVariable("OLJ", lowBound = 0, upBound = None, cat='Continuous')
OHJ = LpVariable("OHJ", lowBound = 0, upBound = None, cat='Continuous')
COJ = LpVariable("COJ", lowBound = 0, upBound = None, cat='Continuous')
RJ = LpVariable("RJ", lowBound = 0, upBound = None, cat='Continuous')

OLFO = LpVariable("OLFO", lowBound = 0, upBound = None, cat='Continuous')
OHFO = LpVariable("OHFO", lowBound = 0, upBound = None, cat='Continuous')
COFO = LpVariable("COFO", lowBound = 0, upBound = None, cat='Continuous')
RFO = LpVariable("RFO", lowBound = 0, upBound = None, cat='Continuous')

RLO = LpVariable("RLO", lowBound = 0, upBound = None, cat='Continuous')


# In[182]:


# Objective Fuction
model += lpSum(Profit[i]*y_vars[i] for i in range(len(Products)))


# In[183]:


# Constraints
for i in range(len(Crude)):
               model += x_vars[i] <= Availability[i]
               
            
model += lpSum(x_vars[i] for i in range(len(Crude)))<= 45000

model += RNL + RNM + RNH <= 10000

model += COL + COH <= 8000


model += y_vars[4] <= 1000

model += y_vars[4] >= 500

model += y_vars[0] >= 0.4*y_vars[1]
         

model += x_vars[0]*0.1 + x_vars[1]*0.15 == NL

model += x_vars[0]*0.2 + x_vars[1]*0.25 == NM

model += x_vars[0]*0.2 + x_vars[1]*0.18 == NH

model += x_vars[0]*0.12 + x_vars[1]*0.08 == OL

model += x_vars[0]*0.2 + x_vars[1]*0.19 == OH

model += x_vars[0]*0.13 + x_vars[1]*0.12 == R

model += RNL*0.6 + RNM*0.52 + RNH*0.45== RG

model += COL*0.68 + COH*0.75 == CO

model += COL*0.28 + COH*0.2 == CG



model += 70*HNRP + 80*MNRP + 90*LNRP + 115*RGRP + 105*CGRP >= 84*y_vars[1]

model += 70*HNPP + 80*MNPP + 90*LNPP + 115*RGPP + 105*CGPP >= 94*y_vars[0]

model += 1*OLJ + 0.6*OHJ + 1.5*COJ + 0.05*RJ <= 1*y_vars[2]

model += y_vars[3]*(10/18) == OLFO

model += y_vars[3]*(4/18) == COFO

model += y_vars[3]*(3/18) == OHFO

model += y_vars[3]*(1/18) == RFO

model += NH == HNRP + HNPP + RNH

model += NM == MNRP + MNPP + RNM

model += NL == LNRP + LNPP + RNL

model += OL == OLJ + OLFO + COL

model += OH == OHJ + OHFO + COH

model += R == RJ + RFO + RLO

model += RG == RGRP + RGPP

model += CO == COJ + COFO

model += CG == CGRP + CGPP

model += HNRP + MNRP + LNRP + RGRP + CGRP == y_vars[1]

model += HNPP + MNPP + LNPP + RGPP + CGPP == y_vars[0]

model += OLJ + OHJ + COJ + RJ == y_vars[2]

model += y_vars[4] == RLO*0.5

model += y_vars[3] == OLFO + COFO + OHFO + RFO


# In[184]:


# Solution 
model.solve()
print(f"status: {model.status}, {LpStatus[model.status]}")


# In[185]:


# Objective Value
print(f"objective: {model.objective.value()}")


# In[186]:


# PRODUCTS of each type
for v in model.variables():
    print(f"{v.name}: {v.value()}")


# In[ ]:





# In[ ]:




