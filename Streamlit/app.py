import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn

@st.cache
def load_data(URL):
    data=pd.read_csv(URL)
    return data

path1="PoetryFoundationData.csv"
path2="all.csv"
selected=0

df_foundation=load_data(path1).iloc[:,1:]
df_analysis=load_data(path2)

st.title("Streamlit course")
st.header("Loading dataframes")

tables_dispo={"Poetry Foundation":df_foundation,"Poetry Analysis":df_analysis}

st.sidebar.title("Selection du data-set à afficher")
option=st.sidebar.selectbox('Data-sets disponibles:',["Poetry Foundation","Poetry Analysis"])
select_table=tables_dispo[option]
len_to_filter=st.sidebar.slider("Nombre de lignes à afficher",1,select_table.shape[0],5)


if st.sidebar.button('Show data'):
    st.subheader('Raw data')
    st.table(select_table.head(len_to_filter))
    selected=1
    
cols=[]    
for col in select_table.columns:
    cols.append(col)
if selected==1:
    st.sidebar.header('Options sur les colonnes')
    st.sidebar.multiselect("Colonnes dispolibles",cols)
    
st.write(0)
    
