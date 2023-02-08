import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly_express as px

global df

def home(uploaded_file):
    if uploaded_file:
        st.header("Begin exploring the data using the menu on the left  ")
        if st.checkbox("Show Table"):
            st.dataframe(df,height=500,width=500)
        if st.button("Click to know number of rows and columns "):
            st.write("The number of rows and columns are ",df.shape)    
    else:
        st.header("To begin please upload a file ")

def stats(dataframe):
    st.header("Data Statistics")
    st.write(dataframe.describe())


def data_header(dataframe):
    st.header("Data Header")
    st.write(df.head())

def plot(dataframe):
    fig,ax=plt.subplots(1,1)
    ax.scatter(x=dataframe["impact.gap"],y=dataframe["impact.magnitude"])
    ax.set_xlabel("Depth")
    ax.set_ylabel("Magnitude")
    st.pyplot(fig)

def interactive(dataframe):
    col1,col2=st.columns(2)
    x_axis_val=col1.selectbox("Select X-axis Value", options=dataframe.columns)
    y_axis_val=col2.selectbox("Select Y-axis Value", options=dataframe.columns)
    cal=st.color_picker("Select a Plot color")

    plot=px.scatter(dataframe,x=x_axis_val,y=y_axis_val)
    plot.update_traces(marker=dict(color=cal))
    st.plotly_chart(plot)

def graph(dataframe):
    col1,col2,col3=st.columns(3)
    x_axis_val=col1.selectbox("Select X-axis Value", options=dataframe.columns)
    y_axis_val=col2.selectbox("Select Y-axis Value", options=dataframe.columns)
    z_axis_val=col2.selectbox("Select z-axis Value", options=dataframe.columns)
    op=st.selectbox("Graphs",["Bar Graph","Line Graph","Area Graph"])
    if op=="Bar Graph":
        data=pd.DataFrame(df,columns=[x_axis_val,y_axis_val,z_axis_val])
        st.bar_chart(data)
    if op=="Line Graph":
        data=pd.DataFrame(df,columns=[x_axis_val,y_axis_val,z_axis_val])
        st.line_chart(data)  
    if op=="Area Graph":
        data=pd.DataFrame(df,columns=[x_axis_val,y_axis_val,z_axis_val])
        st.area_chart(data)  
            

st.title("Data Explorer")
st.text("This is a web app to explore data  ")
# st.header("To begin please upload a file on the left")

st.sidebar.title("Sidebar")

uploaded_file=st.sidebar.file_uploader("Upload a file containing data in the form row and columns ")

options=st.sidebar.radio("Pages",options=["Home","Data Statistics","Data Header","Plot","Interactive Plot","Graphs"])

if uploaded_file:
        
    df=pd.read_csv(uploaded_file)
    st.session_state["df"]=df

  
    
    
if options=="Home":
    home(uploaded_file)
if options =="Data Statistics":
    stats(df)
elif options=="Data Header":
    data_header(df)
elif options=="Plot":
    plot(df)
elif options=="Interactive Plot":
    interactive(df)
elif options=="Graphs":
    graph(df)