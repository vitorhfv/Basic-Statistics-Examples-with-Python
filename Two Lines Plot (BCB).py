#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bcb import sgs


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


pib=sgs.get({'pib':1207}, start = '2003-01-01', end = '2019-12-31')


# In[15]:


pib_am=sgs.get({'pib_am':24114}, start = '2003-01-01', end = '2019-12-31') 


# In[16]:


pib2_am=pib_am.pct_change().mul(100) 
#pct change transforma a variação em porcentagem nos valores da tabela e mul*100 multiplica por 100


# In[17]:


pib2=pib.pct_change().mul(100)


# In[18]:


pib2.head(10)


# In[19]:


plt.style.use('seaborn')
plt.plot(pib2, color='blue')
plt.plot(pib2_am, color='green')
plt.xlabel('ano')
plt.ylabel ('variação percentual (%)')
plt.gca().legend(('PIB do Brasil (%)','PIB do Amazonas (%)'))
plt.title ('PIB do Amazonas e PIB do Brasil')


# In[ ]:




