
# coding: utf-8

# In[88]:


import pandas as pd
import folium
from folium.plugins import HeatMap
from folium import plugins
import gmaps


# In[75]:


data = pd.read_excel('heatmap_buy_20.xlsx')


# In[76]:


new_header = data.iloc[0]
data = data[1:]
data.columns = new_header


# In[77]:


data['latitude']=data.latitude.astype(float)
data['longitude']=data.longitude.astype(float)
data['weight']=data.weight.astype(float)
data.sort_values(by=['weight'], inplace=True)


# In[79]:


print (data)


# In[82]:


intensity = 12
gmaps.configure(api_key="AIzaSyCY...")
m = gmaps.Map()
locations = data[['latitude', 'longitude']]

#coordinates = (22.481918, 88.326035)
#gmaps.figure(center=coordinates, zoom_level=11)

#Get the magnitude from the data
weights = data['weight']


# In[86]:


def drawHeatMap(location, weights, radius):
    # setting the data and parameters
    
    heatmap_layer = gmaps.heatmap_layer(location, weights=weights, dissipating = True)
    heatmap_layer.point_radius = radius
    # draw the heatmap into a figure
    fig = gmaps.figure(layout={
        'width': '900px',
        'height': '550px',
        'padding': '3px',
        'border': '1px solid black'
})
    #fig = gmaps.figure(center = [center_lat,center_lng], zoom_level=zoom)
    fig.add_layer(heatmap_layer)
    return fig


# In[87]:


drawHeatMap(locations,weights, intensity)

