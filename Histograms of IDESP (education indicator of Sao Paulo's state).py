#!/usr/bin/env python
# coding: utf-8

# In[1]:


import basedosdados as bd
import pandas as pd
import seaborn as sbn
import sidetable as stb
import matplotlib.pyplot as plt


# In[2]:


import basedosdados as bd

# Loading the database directly with Pandas
df = bd.read_table(dataset_id='br_sp_seduc_idesp',
table_id='escola',
billing_project_id="bustling-walker-349821")


# In[3]:


df2=df.dropna() # Dropping the null values 
df2.shape


# In[4]:


df2.head(100)


# In[5]:


plt.hist(df2['nota_idesp_ef_iniciais']) 
# Plotting a basic histogram with the grades (elementary and middle school only) of IDESP's indicator using matplotlib.


# In[8]:


df2.describe()


# In[9]:


plt.hist(x='nota_idesp_em', density=True, bins=40, data=df2)
# Plotting a basic histogram with the IDESP indicator notes of the High Schools with matplotlib.


# In[19]:


# Plotting a histogram of IDESP's grades of the High School with Seaborn and Matplotlib.
plt.style.use('seaborn-dark')
plt.figure (figsize=(10,8))
sbn.histplot(y='nota_idesp_em', x='ano', data=df2, bins=25,)
plt.title ('Índice de Desenvolvimento da Educação do estado de SP (Ensino Médio)')
plt.xlabel("ano")
plt.ylabel("Nota do IDESP (Ensino Médio)")
plt.annotate('Fonte: IDESP', (0,0), (0,-20), fontsize=12, 
             xycoords='axes fraction', textcoords='offset points', va='top')


# In[20]:


# You can see that the grades get a litte bit higher (and bluer) through the years, although the median grade still low.
# Thus, you can confirm that there is a improvement of education at São Paulo state between 2008 and 2018.


# In[ ]:




