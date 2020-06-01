#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import folium as fo
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


map=fo.Map()


# In[23]:


map


# In[4]:


x=fo.FeatureGroup(name='My Map')


# In[9]:


x.add_child(fo.Marker(location=[20.2753,73.0073],popup='hey',icon=fo.Icon(color='blue')))


# In[10]:


map.add_child(x)


# In[11]:


for lat,lon in ([34,53],[24,-50],[90,-68]):
    x.add_child(fo.Marker(location=[lat,lon],popup='hey',icon=fo.Icon(color='red')))


# In[13]:


map.add_child(x)


# In[14]:


#plotting volcanoes


# In[5]:


volcano=pd.read_csv('volcano.csv')


# In[7]:


lat_vo=list(volcano['Latitude'])
lon_vo=list(volcano['Longitude'])
name_vol=list(volcano['Name'])


# In[8]:


vol=fo.FeatureGroup(name='My Map')


# In[14]:


for lat,lon,name in zip(lat_vo,lon_vo,name_vol):
    vol.add_child(fo.Marker(location=[lat,lon],
                            popup=name,icon=fo.Icon(color='red')))


# In[15]:


map.add_child(vol)


# In[16]:


#polygon view


# In[18]:


vol.add_child(fo.GeoJson(data=(open('World.json','r',encoding='utf-8-sig').read())))


# In[19]:


map.add_child(vol)


# In[20]:


#Us Cities Population


# In[24]:


popu=pd.read_csv('us cities pop.csv')


# In[25]:


popu.head()


# In[26]:


lat_po=list(popu['lat'])
lon_po=list(popu['lon'])
name_po=list(popu['name'])
pop_po=list(popu['pop'])


# In[27]:


po=fo.FeatureGroup(name='My Map')


# In[31]:


def mar(popu):
    if(popu>35000):
        return 'red'
    elif(popu<10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'
    


# In[32]:


for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name],icon=fo.Icon(color=mar(pop))))


# In[ ]:


map.add_child(po)


# In[ ]:




