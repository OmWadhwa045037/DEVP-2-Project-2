#!/usr/bin/env python
# coding: utf-8

# In[13]:

# In[28]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import numpy as np
from plotly import graph_objects as go


# In[14]:

# In[29]:


st.set_page_config(page_title="DAAWAT Basmati Rice Sales Dashboard",
                  page_icon="bar_chart:",
                  layout="wide")


# In[15]:

# In[30]:


df = pd.read_csv(r"C:\Users\DeLL\OneDrive\Desktop\Daawat Rice Dataset.csv")


# In[16]:

# In[31]:


st.sidebar.header('Please Filter Here:')
Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique())


# In[32]:


Product = st.sidebar.multiselect(
    "Select the Product:",
    options=df["Product"].unique(),
    default=df["Product"].unique())


# In[33]:


Date = st.sidebar.multiselect(
    "Select the Date:",
    options=df["Date"].unique(),
    default=df["Date"].unique())


# In[34]:


df_selection = df.query(
    "Country ==@Country & Product ==@Product & Date ==@Date") 
st.dataframe(df_selection)


# In[17]:

# In[35]:


st.title('DAAWAT Basmati Rice Sales Dashboard')
st.markdown('##')
Total_Unit_Sold= int(df_selection['Units Sold'].sum())
Total_Cost= int(df_selection['Cost'].sum())
Total_Revenue= int(df_selection['Revenue'].sum())
Total_Profit= int(df_selection['Profit'].sum())


# In[18]:

# In[36]:


left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Total Unit Sold')
    st.subheader(f' {Total_Unit_Sold:,}')
with middle_column:
    st.subheader('Total Cost')
    st.subheader(f'US ${Total_Cost:,}')
with middle_column:
    st.subheader('Total Revenue')
    st.subheader(f'US ${Total_Revenue:,}')
with right_column:
    st.subheader('Total Profit')
    st.subheader(f'US ${Total_Profit:,}')
st.markdown("---")


# In[19]:

# In[37]:


sales_by_product = df_selection.groupby(by=['Product']).sum()[['Units Sold']].sort_values(by=['Units Sold'])
fig_Product_sales = px.bar(
    sales_by_product,
    x='Units Sold', y = sales_by_product.index,
    orientation='h', title="<b>Sales by Product</b>",
    color_discrete_sequence=["#0083B8"]* len(sales_by_product),
    template="plotly_white",)


# In[20]:

# In[38]:


bar_chart=px.bar(df_selection, x="Country", y="Units Sold", color="Product", title="Unit Sold Country & Product wise")


# In[39]:


left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart, use_container_width=True)
right_column.plotly_chart(fig_Product_sales, use_container_width=True)


# In[40]:


Pie_chart= px.pie(df_selection, title='Unit Sold Product wise', values='Units Sold', names='Product')
Revenue_Country =px.pie(df_selection, title='Revenue generated Region Wise', values='Revenue', names='Country')


# In[41]:


right_column, middle_column, left_column= st.columns(3)
right_column.plotly_chart(Pie_chart, use_container_width=True)
left_column.plotly_chart(Revenue_Country, use_container_width=True)


# In[21]:

# In[42]:


bar_chart1=px.bar(df_selection, x="Country", y="Revenue", color="Product", title="Total Revenue Country & Product wise")
bar_chart2=px.bar(df_selection, x="Country", y="Profit", color="Product", title="Total Profit Country & Product wise")


# In[43]:


left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart1, use_container_width=True)
right_column.plotly_chart(bar_chart2, use_container_width=True)


# In[22]:

# In[44]:


import plotly.graph_objects as go
map = go.Figure(data=go.Choropleth(
    locations=df['Country'],
    z = df['Units Sold'],
    locationmode = 'country names', 
    colorscale = 'jet',
    colorbar_title = "Units Sold",
))


# In[45]:


map.update_layout(
    title = dict(text = '<b>Units Sold by Countries</b>',
    x = 0.5)
)


# In[46]:


map.show()


# In[23]:

# In[47]:


left_column = st.columns(1)
st.plotly_chart(map, use_container_width=True)


# In[24]:

# hide_st_style = 
# <br>
#             <style><br>
#             #mainMenu {Visibility: hidden;}<br>
#             footer {visibility: hidden;}<br>
#             header {visibility: hidden;}<br>
#             </style><br>
#           
# 

# In[48]:


#st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:
