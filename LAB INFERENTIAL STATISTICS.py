#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


from scipy.stats import ttest_1samp, ttest_rel, ttest_ind
from scipy.stats import f_oneway
from scipy.stats import norm

from statistics import math


# In[7]:


sample_mean = 130.1
pop_mean = 120
pop_std = 21.21
n = 100
alpha = 0.05


# In[6]:


z_score = (sample_mean - pop_mean)/(pop_std/math.sqrt(n)) # differences in mean / standard error
z_score

# Calculate the p value
p_value = norm.cdf(z_score)
p_value


# In[8]:


p_value = norm.cdf(z_score)
p_value



# In[ ]:


# As the p value is  on the critical area ( P value = 99% > critical area > 95% as the alpha is 00.5 or 5%) and we intend to prove that the pop mean is wrong (higher than 120) we can affirm that the pop mean is more than 120. 

