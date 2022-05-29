#!/usr/bin/env python
# coding: utf-8

# In[1]:


import basedosdados as bd

# Para carregar o dado direto no pandas
import pandas as pd
df = bd.read_table(dataset_id='br_ibge_ipca15',
table_id='mes_brasil',
billing_project_id="bustling-walker-349821")


# In[4]:


df.rename(columns={'mes':'mês', 'indice':'índice', 'variacao_mensal':'variação mensal'}, inplace = True)


# In[6]:


df.head(10)


# In[7]:


print (df)


# In[8]:


df.loc[:, 'ano':'índice']


# In[9]:


inf2=df.loc[:,['ano', 'mês', 'índice', 'variação mensal', 'variacao_doze_meses']]


# In[10]:


print (inf2)


# In[11]:


inf01a08=inf2.loc[8:100]


# In[13]:


inf01a08.head()


# In[14]:


inf01a08.describe()


# In[15]:


a = inf01a08['ano']
i = inf01a08['índice']
j = inf01a08['variacao_doze_meses']
v = inf01a08['variação mensal']
y = [2001, 2002, 2003, 2004]


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[112]:


plt.style.use('seaborn-darkgrid')


# In[115]:


plt.figure (figsize=(8,4))
plt.bar (a, j, color='brown')
plt.ylabel ('variação (%)')
plt.xlabel('ano')
plt.title ('Variação anual do IPCA (%) do Brasil')
plt.style.library['seaborn-darkgrid']
plt.axis ([2000, 2009, 1, 18])

plt.show()

