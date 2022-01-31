#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 22:19:06 2022

@author: anak
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import warnings


warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

data = pd.read_excel(r"./data_sortie.xlsx")

plt.style.use("dark_background")

st.image(r"./net.jpeg", use_column_width=True)
colT1,colT2 = st.columns([2,8])

with colT2:
    st.title("🎬 RATING PREDICTION 🎬" ) 
st.markdown("### Description")
st.markdown("The goal of this project is to practice in supervised learning using Netflix data. We create a model for the rating prediction")

st.sidebar.image(r"./netflixa.jpeg")
st.sidebar.write("### 🍿 Welcome 🍿!")
st.sidebar.write("You can set up different display options here below")
st.sidebar.write("")
st.sidebar.write("##### Please select the Model you would like to analyze")   

          
quadratic = st.sidebar.checkbox('Quadratic Discriminant Analysis')
gaussian = st.sidebar.checkbox('Gausssian NB') 
decision = st.sidebar.checkbox('DecisionTreeClassifier')
voting = st.sidebar.checkbox('VotingClassifier')
comparison= st.sidebar.checkbox('Comparison All Models')
Thankyou=st.sidebar.checkbox('Thank you')
st.sidebar.write("")
st.sidebar.write("")



#Number of movies per year
#Movies per country
#The most popular genre per year
#The most popular genre per country

with st.container():
    st.markdown("### Number of movies per year")
    col1, col2= st.columns([2,1])
    
    with col1:
        datafilm=data[['title','year']].groupby('year',as_index=False).agg('count')               
        fig = px.line(datafilm, x="year", y="title",labels={'title':'Number of Movies'},title='Number of movies per year')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.image(r"./gif5.gif", use_column_width=True)
        
        
with st.container():
    st.markdown("### Movies per country")
    col1, col2= st.columns([1,2])
    
    with col2:
        datafilm=data[['title','Country']].groupby('Country',as_index=False).agg('count')               
        fig = px.bar(datafilm, x="Country", y="title", color='Country',labels={'title':'Number of Movies'},title='Number of movies per Country')
        st.plotly_chart(fig, use_container_width=True)
        
    with col1:
        st.image(r"./gif1.gif", use_column_width=True)
    

with st.container():
    st.markdown("### The Most Popular Genre per Year")
    col1, col2= st.columns([2,1])
    
    with col1:
        most_genress = pd.DataFrame()
        df1 = data[['year', 'title', 'Genre']]
        # groupby table
        group_tab = df1.groupby(['year', 'Genre'], as_index=False)[['Genre','title']].agg({'title':'count'})
        # new df with max count by genre and countries
        years = group_tab['year'].unique()
        for year in years:
            d = group_tab[(group_tab['year'] == year)]
            d = d[(d['title'] == d['title'].max())]
            most_genress = pd.concat([most_genress, d], ignore_index=True)
              
        fig = px.bar(most_genress, x='year', y='title',hover_data=['Genre'],color='Genre',labels={'title':'Number of Movies'},title="The most popular Genre per Year")
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.image(r"./gif2.gif", use_column_width=True)
        

with st.container():
    st.markdown("### The Most Popular Genre per Country")
    col1, col2= st.columns([2,1])
    
    with col1:
        most_genres = pd.DataFrame()
        df1 = data[['Country', 'title', 'Genre']]
        # groupby table
        group_tab = df1.groupby(['Country', 'Genre'], as_index=False)[['Genre','title']].agg({'title':'count'})
        # new df with max count by genre and countries
        countries = group_tab['Country'].unique()
        for country in countries:
            d = group_tab[(group_tab['Country'] == country)]
            d = d[(d['title'] == d['title'].max())]
            most_genres = pd.concat([most_genres, d], ignore_index=True)
              
        #fig = px.bar(most_genress, x='year', y='title',hover_data=['Genre'],color='Genre',labels={'title':'Number of Movies'},title="The most popular Genre per Year")
        
        fig = px.treemap(most_genres, path=[px.Constant('Country'), 'Country','Genre'], values='title',
                  color='Country', hover_data=['title'])

        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.image(r"./gif3.gif", use_column_width=True)
        
with st.container():
    st.markdown(" ")
    st.markdown("### Prediction Model")
    
    if quadratic == True:
       st.image(r"./model1.png", use_column_width=True)
       st.markdown(" ")
        
    if gaussian:
        st.image(r"./model2.png", use_column_width=True) 
        st.markdown(" ")
    
    if decision:
        st.image(r"./model4.png", use_column_width=True)
        st.markdown(" ")

    if voting:
        st.image(r"./model3.png", use_column_width=True)
        st.markdown(" ")
        

    if comparison == True:
         with st.container():
                 st.markdown("")
                 st.markdown("### Comparison of All Models")
                 conclusion=pd.DataFrame()
                 conclusion['Accuracy %']=[42.7,32.4,32.4,21.5]
                 conclusion['Precision %']=[32.9,32.9,27.3,24.5]
                 conclusion['Recall %']=[30,27.7,32.4,20.3]
                 conclusion['F1 %']=[31.7,28.1,18.2,16.1]
                 conclusion['AUC']=[0.3,0.1,0.63,0.19]
                 conclusion.index=['DecisionTreeClassifier','VotingClassifier','GaussianNB','Quadratic Discriminant Analysis']
                 st.table(conclusion)
                 
                 fig = px.histogram(conclusion,x=conclusion.index,y=conclusion.columns, barmode='group')
                 
                 st.plotly_chart(fig, use_container_width=True)
                 st.markdown(" ")
         
        

    if Thankyou:
        st.markdown(" ")
        col1, col2= st.columns([1,2])
        with col1:
            st.markdown("# Thank you! 😊 ")
            
        with col2:    
            st.image(r"./gif4.gif", use_column_width=True)
        
               