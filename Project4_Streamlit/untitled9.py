#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:45:27 2022

@author: anak
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
from sklearn import datasets
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import plotly.graph_objects as go
import warnings
import streamlit as st
from bokeh.plotting import figure
import squarify
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

data = pd.read_csv(r"./dataset.csv")


plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '#000000'  # very light grey

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#86EAE9'  # bluish dark grey
    
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.serif'] = 'Abramo'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 5
plt.rcParams['axes.labelsize'] = 3
plt.rcParams['axes.titlesize'] = 3
plt.rcParams['xtick.labelsize'] = 3
plt.rcParams['ytick.labelsize'] = 3
plt.rcParams['legend.fontsize'] = 3
plt.rcParams['figure.titlesize'] = 6



st.image(r"./ima1.png", use_column_width=True)
colT1,colT2 = st.columns([2,8])
with colT2:
    st.title("PATIENT SURVIVAL PREDICTION") 
st.markdown("### Description")
st.markdown("The predictors of in-hospital mortality for admitted patients remain poorly characterized. We aimed to develop and validate some KPI model for all-cause in-hospital mortality among admitted patients.")


st.sidebar.write("### Welcome 🤒!")
st.sidebar.write("You can set up different display options here below")
st.sidebar.write("")
st.sidebar.write("##### Please select the data you would like to analyze for General Data Section")                
agreeh = st.sidebar.checkbox('Number of Hospitals')
agreep = st.sidebar.checkbox('Number of Patients') 
agreed = st.sidebar.checkbox('Number of ICU') 
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("##### Please select the Gender you would like to analyze for sections below")
st.sidebar.write("- Patient Information")
st.sidebar.write("- Previous diseases")
makes=['Female','Male','All']
make_choice = st.sidebar.selectbox('Select the Gender :', makes)
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("##### Please select the Ethnicity you would like to analyze for sections below")
st.sidebar.write("- ICU Deaths")
makes2=['All','African American','Asian','Caucasian','Hispanic','Native American','Other/Unknown' ]
make_choice2 = st.sidebar.selectbox('Select the Ethnicity:', makes2)



################# Scatter Chart Logic #################




with st.container():
    st.markdown("### General Data")
    st.markdown("##### Data you would like to analyze")
    col1, col2, col3 = st.columns(3)
                           
    if agreeh:
        col1.metric("Number of Hospitals", "147 🏥")
    if agreep:
        col2.metric("Patients", "91713","54% 👨  46%👩" )
    if agreed:
        col3.metric("Number of ICU", "241 ⚕️ ")



set1= data[['age','ethnicity', 'gender','bmi','patient_id']]
bmi_range=[]
for i in set1['bmi']:
    if i < 18.5:
        bmi_range.append('Underweight')
    elif i > 18.5 and i < 24.9:
        bmi_range.append('Healthy')
    elif i > 25  and i< 29.9:
        bmi_range.append('Overweight')
    else:
        bmi_range.append('Obese')
set1['bmi_range']=bmi_range

E= set1.groupby(['ethnicity', 'gender']).age.count().unstack()



set2=pd.DataFrame()

if make_choice=='All':
    lables = ['Female','Male']
    set2=set1
    #for gausian
    values_0=73
    values_1=25
    values_2=3
    data2=data
if make_choice=='Female':
    set2=set1[set1['gender']=='F']
    lables = ['Female']
    values_0=39
    values_1=11
    values_2=2
    data2=data[data['gender']=='F']
if make_choice=='Male':
    set2=set1[set1['gender']=='M']
    lables=['Male']
    values_0=34
    values_1=14
    values_2=1
    data2=data[data['gender']=='M']





    
    

with st.container():
    st.markdown("")
    st.markdown("")
    st.markdown("### Patient Information")
    st.markdown("#### Content")
    st.markdown("📈 Weight and BMI Categories")
    st.markdown("👥 Ethnicity")
    st.markdown("📅 Age")           
    st.markdown("")
    st.markdown("")    
    
    st.markdown("##### 📈  Weight and BMI Categories")

    col1, col2 = st.columns([3, 1])


    st.markdown("")

    with col2:
        col2.subheader("BMI Categories")
        data5={'Category':['Underweight','Healthy','Overweight','Obese']}
        bmi=pd.DataFrame(data5,index=['<18.5','18.5 - 24.9','25-29.9','>29.9'])
        st.table(bmi)
    
    with col1:
        col1.subheader("Number of Patients per BMI Category" )
        BMIC= set2[['bmi_range', 'gender']].groupby(['bmi_range']).agg('count')
        st.bar_chart(BMIC,use_container_width=True)    
    
    

st.markdown("")


st.markdown("#### 👥  Ethnicity")
with st.container():
    
    col1, col2= st.columns([1,2])

    with col1:
        
        col1.subheader("Ethnicity Distribution")
        B= set2[['ethnicity', 'gender']].groupby(['ethnicity'],as_index=False).agg('count')
        B['Percentage']=round((B['gender']/B['gender'].sum())*100)
        base = alt.Chart(B).encode(
        theta=alt.Theta("Percentage:Q", stack=True),
        radius=alt.Radius("Percentage", scale=alt.Scale(type="sqrt", zero=True, rangeMin=70)),
        color="ethnicity:N")
        
        c1 = base.mark_arc(innerRadius=20, stroke="#fff")
        c2 = base.mark_text(radiusOffset=10).encode(text="Percentage:Q")
        c1 + c2

    with col2:
        st.image(r"./ima2.png", use_column_width=True)
        
st.markdown("")

st.markdown("#### 📅 Age")
with st.container():

    
    st.subheader("Age Distribution")
    values_bins = st.slider('Please Select The number of bins to analyze the age',
         1, 10, (1))
    st.write('You chose:', values_bins)
    

    lista5=[]
    l=int(100/values_bins )
    bins=[]
    value=0
    for i in range(0,values_bins +1):
        
        value=i*l
        bins.append(value)
    set3=set2
    set3['category'] = pd.cut(set3['age'], bins=bins)
    counts = set3.groupby(['category', 'gender'],as_index=False).age.count()

    leng=len(counts['category'])
    if make_choice=='All':
        leng=int(leng/2)
    for i in range(0,leng):
        lista5.append(str(bins[i])+"-"+str(bins[i+1]))
        if make_choice=='All':
            lista5.append(str(bins[i])+"-"+str(bins[i+1]))
        
    counts['Age Ranges']=lista5
    
    gra= alt.Chart(counts).mark_bar().encode(
        x=alt.X('sum(age)',title='Frequency'),
        y=alt.Y('Age Ranges', title='Age Ranges'),
        color=alt.Color('gender', title='Gender')
        )
    
    st.altair_chart(gra,use_container_width=True)


#ICU ACCESS
st.markdown("")
st.markdown("")
st.markdown("### Intensive Care Unit Admission Source")
st.markdown("Information about the reasons the patient access to ICU")         


with st.container():
    col1, col2= st.columns([1,1])
    with col1:
        
        df= data2[["icu_admit_source","patient_id"]].groupby(["icu_admit_source"],as_index=False).agg("count")
        fig = px.treemap(
        df,
        parents=['Source','Source','Source','Source','Source'],
        names='icu_admit_source',
        values='patient_id',)
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        
        fig = px.sunburst(
        df,
        parents=['Source','Source','Source','Source','Source'],
        names='icu_admit_source',
        values='patient_id',
        )
        st.plotly_chart(fig, use_container_width=True)


#Previous diseases


st.markdown("")
st.markdown("")
st.markdown("### Previous Diseases")
st.markdown("Information about the diseases patient were diagnosed before accessing to ICU") 


with st.container():
    
    col1, col2,col3= st.columns([1,1,1])

    with col1:
        
        fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = values_0,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "% of Patients with No Previous Diseases"}))
        st.plotly_chart(fig,use_container_width=True)
    
    with col2:

        fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = values_1,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "% of Patients with One Previous Disease"}))
        st.plotly_chart(fig,use_container_width=True)

    with col3:
        fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = values_2,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "% of Patients with Two Previous Diseases"}))
        st.plotly_chart(fig,use_container_width=True)







with st.container():
    
    st.subheader("Previous Diseases Distribution")

    diseases=data2[['aids','cirrhosis','diabetes_mellitus','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis','gender']].groupby('gender',as_index=False).agg('sum')
    disease= ['aids','cirrhosis','diabetes_mellitus','hepatic_failure','immunosuppression','leukemia','lymphoma','solid_tumor_with_metastasis']
    diseases2=diseases.melt(id_vars=["gender"],var_name="Diseases",value_name="Value")
    
    fig=alt.Chart(diseases2).mark_bar(opacity=0.7).encode(
    x=alt.X('Diseases',title='Diseases'),
    y=alt.Y('sum(Value)',title='Frequency'),
    color=alt.Color('gender', title='Gender')
    )
     
    st.altair_chart(fig,use_container_width=True)
    
with st.container():   
    
    
    st.subheader("% Previous Diseases")
    
    order=diseases2[['Value','Diseases']].groupby(['Diseases']).agg('sum')
    order=order.sort_values(by='Value',ascending=False)
    fig = px.funnel_area(names= list(order.index),values=list(order['Value']))
    st.plotly_chart(fig, use_container_width=True)


    




  
st.markdown("")
st.markdown("")
st.markdown("### ICU Deaths ☠️")
st.markdown("Information about the patients that died during their stay in ICU") 




if make_choice2=='All':
    lables = ['African American','Asian','Caucasian','Hispanic','Native American','Other/Unknown' ]
    set2=data
if make_choice2=='African American':
    set2=data[data['ethnicity']=='African American']
    lables = ['African American']
if make_choice2=='Asian':
    set2=data[data['ethnicity']=='Asian']
    lables = ['Asian']
if make_choice2=='Caucasian':
    set2=data[data['ethnicity']=='Caucasian']
    lables = ['Caucasian']
if make_choice2=='Hispanic':
    set2=data[data['ethnicity']=='Hispanic']
    lables = ['Hispanic']
if make_choice2=='Native American':
    set2=data[data['ethnicity']=='Native American']
    lables = ['Native American']
if make_choice2=='Other/Unknown':
    set2=data[data['ethnicity']=='Other/Unknown']
    lables = ['Other/Unknown']
    
    
with st.container():
    col1, col2= st.columns([2,1])
    
    with col1:
        
        col1.subheader("Death Patients - Ethnicity - Gender")
        g=set2.groupby(['ethnicity','gender'],as_index=False).agg({'hospital_death':'count'})
    
    
        fig = px.bar(g, x="ethnicity", y="hospital_death", color="gender",
                 pattern_shape="gender", pattern_shape_sequence=[".", "x"])
    
        
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        
        col2.subheader("Deaths Patients - Gender")
        
        g=set2.groupby(['gender'],as_index=False).agg({'hospital_death':'count'})
        
        fig = px.bar(g, x="gender", y="hospital_death", color="gender",
                 pattern_shape="gender", pattern_shape_sequence=["+", "x"])
        
        st.plotly_chart(fig,use_container_width=True)



#Waiting Time before ICU


st.markdown("")
st.markdown("")
st.markdown("### Waiting Time Before Access to the ICU ⏳")
st.markdown("Information about the days patients spent at the hospital before accessing to ICU") 

with st.container():
    col1, col2= st.columns([1,2])
    
    with col1:
        
        source = pd.DataFrame([
              {'Time': '0-1', 'percentage': 20.4,'timesy': 'times'},
              {'Time': '1-2', 'percentage': 20,'timesy': 'times'},
              {'Time': '2-3', 'percentage': 20,'timesy': 'times'},
              {'Time': '3-4', 'percentage': 20,'timesy': 'times'},
               {'Time': '4-5', 'percentage': 12.4,'timesy': 'times'},
             {'Time': '5-6', 'percentage': 7.9,'timesy': 'times'},
                   {'Time': '6-7', 'percentage': 4.3,'timesy': 'times'},
             {'Time': '7-8', 'percentage': 2.6,'timesy': 'times'}
             ])
        
        source['percentage']=(source['percentage']/10)
        # add emoji column
        source['emoji'] =[{'times':'⏳'}[timess] *int(percentage) for timess,percentage in source[['timesy','percentage']].values ]
        
        gras=alt.Chart(source).mark_text(align='left').encode(
            alt.X('percentage:O',scale=alt.Scale(range=[0,100])),
            alt.Y('timesy:O', axis=None),
            alt.Row('Time:N', header=alt.Header(title='Days')),
            alt.SizeValue(30),
            text='emoji'
        ).properties(width=400, height=40
        ).transform_calculate(
           percentage='0'
        )
            
        st.altair_chart(gras,use_container_width=True)
        
        
    with col2:
        st.image(r"./ima3.png", use_column_width=True)