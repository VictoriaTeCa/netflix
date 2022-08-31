import pandas as pd
import numpy as np
import streamlit as st
import codecs 

data= pd.read_csv('movies.csv') 
data

doc = codecs.open('movies.csv','rU','latin1')

sidebar = st.sidebar
sidebar.title("Filtros:")

st.title ("Netflix App")

agree = st.sidebar.checkbox("Mostrar todos los filmes")
if agree:
  st.dataframe(data)






#selected_director = st.sidebar.selectbox("Seleccionar Director", data['director'].unique())
#st.write(f"Selected Option: {selected_director!r}")

@st.cache
def load_data_bydirector(director):
    data= pd.read_csv('movies.csv') 
    #filtered_data_byname= data[data ["name"].str.contains(name)]
    filtered_data_bydirector = data[data['director']==(director)]

    return filtered_data_bydirector

director = st.sidebar.selectbox("Seleccionar Director", data['director'].unique())
btnDirector= st.sidebar.button("Buscar por director")

if (btnDirector):
    selected_director=load_data_bydirector(director)
    count_row=selected_director.shape[0]
    st.write(f"total directores: {count_row}")

    st.dataframe(selected_director)




#selected_filmes = st.sidebar.radio("Seleccionar filme", data['name'].unique())
#st.write("Seleccionar filme:", selected_filmes)

#st.write(data.query(f"""name==@selected_filmes"""))

#st.markdown("_")

@st.cache
def load_data_byname(name):
    data= pd.read_csv('movies.csv') 
    #filtered_data_byname= data[data ["name"].str.contains(name)]
    filtered_data_byname = data[data['name'].str.upper().str.contains(name.upper())]

    return filtered_data_byname


name=st.sidebar.text_input("Bucar por nombre")
btnName= st.sidebar.button("Bucar por nombre")


if (name):
    filterbyname=load_data_byname(name)
    count_row=filterbyname.shape[0]
    st.write(f"total names: {count_row}")

    st.dataframe(filterbyname)




