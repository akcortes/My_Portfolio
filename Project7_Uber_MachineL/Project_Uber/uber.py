#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:58:30 2022

@author: anak
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
import folium
from streamlit_folium import folium_static
import datetime



warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

data = pd.read_csv(r"/Users/anak/Downloads/final_data.csv")


st.image(r"/Users/anak/Downloads/uber1.png", use_column_width=True)
colT1,colT2 = st.columns([2,8])

with colT2:
    st.title("UBER RIDES" ) 
st.markdown("### Description")
st.markdown("The goal of this project is to practice in unsupervised Machine learning models. We will imagine we are Uber and we want to give recommendations on where drivers should be to maximize their chances of finding a ride. We will use Machine Learning to create this recommendation algorithm.")

st.sidebar.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber2.png")
st.sidebar.write("### Welcome 🚕!")
st.sidebar.write("You can set up different display options here below")
st.sidebar.write("")
st.sidebar.write("##### Please select the Model you would like to analyze")   

          

kmeans = st.sidebar.checkbox('KMEANS') 
hiera = st.sidebar.checkbox('HierarchicalClassifier')
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write('Recommendations 🕵️')
day = st.sidebar.checkbox('Day of the week')
hour= st.sidebar.checkbox('Hour')
both= st.sidebar.checkbox('Hour + Day of the Week')


#Number of movies per year
#Movies per country
#The most popular genre per year
#The most popular genre per country

with st.container():
    st.markdown("### Cluster Distribution")
    col1, col2= st.columns([2,1])
    
    with col1:
        Xdb = data[['Lat','Lon']]
        ydb = data['db_clusters']
        fig=px.scatter(data, x="Lat", y="Lon",color='db_clusters',title='Cluster Distribution')        
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber3.jpeg", use_column_width=True)
       

with st.container():
    st.markdown("### Cluster Information")
    clusts= data.groupby(['db_clusters'], as_index=False)[['Lat','Lon']].agg(['mean','count'])
    clusts.reset_index(inplace=True)
    clusts['radius']= ''
    clusts['radius']=round(clusts['Lon','count']/sum(clusts['Lon','count'])*100,0)
    clusts         

with st.container():
    st.markdown(" ")
    st.markdown("### Cluster Radio")  
    st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/mapuber.png", use_column_width=True) 
    
    
with st.container():
    st.markdown(" ")
    st.markdown(" ")
    st.markdown("### Rides Distribution %")
    col1, col2= st.columns([1,2])

    
    with col1:
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber4.jpeg", use_column_width=True) 
    
    with col2:
        d=pd.DataFrame()
        d=data['db_clusters'].value_counts()
        fig = px.pie(d, values=d.values, names=['Manhattan','Queens','JFK Airport','Newark Airport'],title='Percentage of Rides/Cluster')
        st.plotly_chart(fig, use_container_width=True)
    





if kmeans:
    with st.container():
        st.markdown(" ")
        st.markdown("### KMEANS Elbow")  
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/kmeans_elbow.png", use_column_width=True)
     
    with st.container():
        st.markdown(" ")
        st.markdown("### KMEANS Scatter")  
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/KMeans6_scatter.png", use_column_width=True)
        
        
    with st.container():
        st.markdown(" ")
        st.markdown("### KMEANS Map")  
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/kmeans_map.png", use_column_width=True)
        
  
    


if hiera:
    with st.container():
        st.markdown(" ")
        st.markdown("### Dendogram")  
        st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/HC_Dendrogram.png", use_column_width=True)

















with st.container():
    st.markdown(" ")
    st.markdown("### Recommendations 💡" )
    
    if day:
        with st.container():
            st.markdown("### Recommendations About the Day of the Week 📅 " )
            
            col1, col2,col3= st.columns([1,1,1])
            with col1:
            
                data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%Y/%m/%d %H:%M:%S')
                data['day']=data['Date/Time'].dt.day_name()
                data2=pd.DataFrame()
                data2=data
                if st.button("All"):
                    data2=data
                
                if st.button('Manhattan'):
                    data2=data[data['db_clusters']==0]
                    
                if st.button('Queens'):
                    data2=data[data['db_clusters']==-1]
                    
                if st.button('JFK Airport'):
                    data2=data[data['db_clusters']==1]
                    
                if st.button('Newark Airport'):
                    data2=data[data['db_clusters']==2]
                
            with col2:    
            
                days=data2[['day','db_clusters']].groupby('day').agg('count')
                days = days.rename(columns={'db_clusters':'Rides'})
                days
                
            with col3:
                st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber8.png", use_column_width=True)
                
        with st.container():
            fig=px.bar(days, x=days.index, y="Rides",color=days.index,labels={'Rides':'Number of Rides'}, height=400,text_auto=True)
            st.plotly_chart(fig, use_container_width=True)
    

    if hour:
        with st.container():
            st.markdown("### Recommendations About the Hours ⌚" )
            
            col1, col2,col3= st.columns([1,1,1])
            with col1:
                data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%Y/%m/%d %H:%M:%S')
                data["Hour"]= data['Date/Time'].dt.hour
                data3=pd.DataFrame()
                data3=data
                if st.button("All "):
                    data3=data
                
                if st.button('Manhattan '):
                    data3=data[data['db_clusters']==0]
                    
                if st.button('Queens '):
                    data3=data[data['db_clusters']==-1]
                    
                if st.button('JFK Airport '):
                    data3=data[data['db_clusters']==1]
                    
                if st.button('Newark Airport '):
                    data3=data[data['db_clusters']==2]
                
            with col2:    
            
                hoursd=data3[["Hour",'db_clusters']].groupby("Hour").agg('count')
                hoursd = hoursd.rename(columns={'db_clusters': 'Rides'})
                hoursd
                
            with col3:
                st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber7.png", use_column_width=True)
                
        with st.container():
            fig=px.bar(hoursd, x=hoursd.index, y="Rides",color=hoursd.index,labels={"Rides":'Number of Rides'}, height=400,text_auto=True)
            st.plotly_chart(fig, use_container_width=True)

    if both:

        with st.container():
            st.markdown("### Recommendations About the Hours ⌚ and Day of the Week 📅 " )
            
            col1, col2= st.columns([1,1])
            with col1:
                data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%Y/%m/%d %H:%M:%S')
                data["Hour"]= data['Date/Time'].dt.hour
                data['day']=data['Date/Time'].dt.day_name()
                data4=pd.DataFrame()
                data4=data
                if st.button("All  "):
                    data4=data
                
                if st.button('Manhattan  '):
                    data4=data[data['db_clusters']==0]
                    
                if st.button('Queens  '):
                    data4=data[data['db_clusters']==-1]
                    
                if st.button('JFK Airport  '):
                    data4=data[data['db_clusters']==1]
                    
                if st.button('Newark Airport  '):
                    data4=data[data['db_clusters']==2]
                

                
                
            with col2:
                st.image(r"./app/my_portfolio/Project7_Uber_MachineL/Project_Uber/uber9.jpeg", use_column_width=True)
                
        with st.container():
            hourc = st.slider('Hour',min_value=0,max_value=23,step=1)
            data5=data4[data4['Hour']==hourc]
            
            hoursd2=data5[["Hour",'db_clusters','day']].groupby(["Hour",'day'],as_index=False).agg({'db_clusters':'count'})
            fig=px.bar(hoursd2, x='day', y="db_clusters",color='day',labels={'db_clusters':'Number of Rides'}, height=400,text_auto=True)
            st.plotly_chart(fig, use_container_width=True)



             
