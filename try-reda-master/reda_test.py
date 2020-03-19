#!/usr/bin/env python
# coding: utf-8

# # REDA Example Notebook

# ## Setup

# In[1]:


# In case you want to try the newest version from git.
# Please be aware that this may break this notebook
# !pip install git+git://github.com/geophysics-ubonn/reda


# In[3]:

import os 
import reda
os.chdir(r'E:\Padova\Z_Database\db_git\D_reda_import\agrogeophy-data\try-reda-master')
import pandas as pd
pd.set_option('display.width', 1000)

# get_ipython().run_line_magic('matplotlib', 'inline')
import reda.utils.mpl
plt, mpl = reda.utils.mpl.setup()

import numpy as np
np.random.seed(2017)

from glob import glob


# ## Usage of reda

# In[5]:


# get list of data files
data_files = sorted(glob('data/pygimli_*.ohm'))
# take only each tenth data file
data_files = data_files[0:-1:10]


# In[6]:


from reda import ERT

obj = ERT()

for nr, filename in enumerate(data_files):
    obj.import_bert(filename, timestep=nr)
  
obj.compute_K_analytical(spacing=1)


# In[7]:


# hack together reciprocals
import pandas as pd
data_rec = obj.data.values
dfr = pd.DataFrame(
    np.hstack((data_rec[:, 2:4], data_rec[:, 0:2], data_rec[:, 4:])),
    columns=obj.data.columns
)

# need to set the data types accordingly
for key, dtype in obj.data.dtypes.items():
    dfr[key] = dfr[key].astype(dtype)

print(dfr.head(5))

# add some noise
dfr['rho_a'] = dfr['rho_a'] + 0.05 * dfr['rho_a'].values * np.random.randn(dfr.shape[0])
obj.data = pd.concat((obj.data, dfr))


# In[8]:


print(obj.data.head(10))


# In[9]:


# these timesteps where imported
print(obj.data.groupby('timestep').groups.keys())


# ## Filtering data

# In[10]:


# apply to all timesteps
# obj.filter('K > 1000')


# In[11]:


# apply only to timestep 10
obj.sub_filter(
    'timestep in [3, 7]',
    'a > 10 and a < 20 and k > 1000',    
)


# In[12]:


print(obj.data.query('timestep == 3 and rho_a < 200'))


# ## Histogram plotting

# In[13]:


obj.data.dtypes


# In[14]:


import reda.plotters.histograms as RH
fig = RH.plot_histograms_extra_dims(
    obj,
    keys=['rho_a', ],
    extra_dims=['timestep', ],
    Nx=5,
    #subquery='timestep in {0}'.format(list(range(0, 100, 10))),
    subquery='timestep in [0, 3, 6]'
)
# print(fig.get_figwidth(), fig.get_figheight())
# fig.savefig('histogram.png', dpi=300)


# ## Plotting Pseudosections

# In[15]:


import reda.plotters.pseudoplots as PS
fig = PS.plot_ps_extra(
    obj, 'rho_a',
    subquery='timestep in [0, 3, 6]'
)
fig.set_size_inches(7.87, 3.93)
fig.tight_layout()
fig.savefig('pseudoplots.png', dpi=600)


# ## Analyzing time series

# In[16]:


import reda.plotters.time_series as TS

fig, ax = TS.plot_quadpole_evolution(
    obj,
    [10, 11, 15, 14],
    'rho_a',
    threshold=0.05,
    rolling=False,
)


# In[17]:


# add some noise to the data
import numpy as np
np.random.seed(2017)
obj.data['rho_a'] = obj.data['rho_a'] + (np.abs(obj.data['rho_a'] * 0.05 * np.random.randn(obj.data.shape[0])))


# In[18]:


fig, ax = TS.plot_quadpole_evolution(
    obj,
    [10, 11, 15, 14],
    'rho_a',
    threshold=0.05,
    rolling=False,
)


# ## The Data Journal

# In[19]:


obj.print_data_journal()
obj.print_data_journal_2file()

# In[ ]:




