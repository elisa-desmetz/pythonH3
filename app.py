import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib
import matplotlib.pyplot as plt
import os
from scipy import stats
from scipy.stats import norm

st.set_option('deprecation.showPyplotGlobalUse', False)

# Chargement du dataset par path
@st.cache
def load_data(URL):
    data=pd.read_csv(URL, encoding='ISO-8859-1')
    if "Unnamed: 0" in data.columns:
        data.drop(['Unnamed: 0'],axis=1,inplace=True)
    return data

# Récupération du path du dossier de travail et des .csv qu'il contient
cur_dir=os.getcwd()
files={}
def walk_through_files(path, file_extension='.csv'):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_extension): 
                files[filename]=os.path.join(dirpath, filename)
walk_through_files(cur_dir)

# Affichage des titres
st.title("Streamlit course")
st.header("Loading dataframes")

# Mise en forme du menu déroulant de sélection de la base de donnée
options_tables=[]
for n in files.keys():
    options_tables.append(n)
st.sidebar.title("Data-sets disponibles")
option_table=st.sidebar.selectbox('',options_tables)
select_table=load_data(files[option_table])

numeric_table=select_table[select_table.select_dtypes(include=[np.number]).columns]
others_table=select_table[select_table.select_dtypes(exclude=[np.number]).columns]

# Menu d'options
exp_options=st.sidebar.beta_expander("Options d'affichage",False)
with exp_options:
    len_to_filter=exp_options.slider("Nombre de lignes à afficher",1,select_table.shape[0],5)
    opt_type=exp_options.checkbox("Types des variables en colonne", key=1)
    opt_taille=exp_options.checkbox("Taille du data-set", key=2)



if st.sidebar.button('Show data'):
    if (opt_type or opt_taille):
        col1, col2 = st.beta_columns((2,1))
        col1.subheader('Raw data')
        col1.dataframe(select_table.head(len_to_filter),height=800)
        if opt_type:
            col2.subheader('Type des colonnes')
            col2.write(select_table.dtypes)
        if opt_taille:
            col2.subheader('Taille du data-set')
            col2.write("Le data-set comporte {} variables sur {} observations.".format(str(select_table.shape[1]),str(select_table.shape[0])))
    else:
        st.subheader('Raw data')
        st.dataframe(select_table.head(len_to_filter),height=800)
    
cols=[]   
name_cols=[]
for col in select_table.columns:
    cols.append(col)
    name_cols.append(str(col).capitalize())
                     
st.sidebar.header('Affichage de colonnes spécifiques')
option_col=st.sidebar.multiselect("Colonnes dispolibles",cols)

if st.sidebar.button('Show columns'):
    if option_col==[]:
        st.warning('Aucune colonne sélectionnée. \n \n Veuillez sélectionner des colonnes à afficher via le menu associé.')
    else:
        col1, col2 = st.beta_columns((2,1))
        col1.subheader('Colonnes filtrées')
        col1.write(select_table[option_col],height=800)
        col2.subheader('Type des colonnes')
        col2.write(select_table[option_col].dtypes)

st.sidebar.header('Statistiques descriptives')
exp_descriptives=st.sidebar.beta_expander("Tables résumées",False)
with exp_descriptives:
    opt_detail=exp_descriptives.checkbox("Résumé détaillé")
    opt_manquant=exp_descriptives.checkbox("Données manquantes")

exp_graphiques=st.sidebar.beta_expander("Représentations graphiques",False)
with exp_graphiques:    
    opt_outliers=exp_graphiques.checkbox("Distribution et outliers")
    opt_heatmap=exp_graphiques.checkbox("Matrice de corrélation")

    
       
if st.sidebar.button('Afficher les informations'):
    if not (opt_detail or opt_manquant or opt_outliers or opt_heatmap):
        st.warning('Aucune option sélectionnée. \n \n Veuillez sélectionner des options à afficher via le menu associé.')
    if not numeric_table.empty:
        if opt_detail:
            st.subheader("Données numériques")
            st.dataframe(numeric_table.describe())
        if opt_outliers:
            st.subheader("Distribution et outliers")
            for col in numeric_table.columns:
                std = np.std(numeric_table[col], ddof=1)
                mean = np.mean(numeric_table[col])

                fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(8,4))

                domain = np.linspace(np.min(numeric_table[col]), np.max(numeric_table[col]))
                ax1.plot(domain, norm.pdf(domain, mean, std), color='darkgreen')
                ax1.hist(numeric_table[col], edgecolor = 'black', alpha = 0.5, density = True, color='lime')
                ax1.set(xlabel=str(col), ylabel='Densité')


                ax2.boxplot(numeric_table[col])
                ax2.set(xlabel=str(col))
                plt.show()

                st.pyplot() 
        if opt_heatmap:
            cont_vars = list(numeric_table.columns)
            mask = np.triu(numeric_table[cont_vars].corr())
            plt.figure(figsize=(11,11))
            sn.heatmap(numeric_table[cont_vars].corr(), annot=True, fmt='.2g', 
            vmin=-1, vmax=1, center=0, cmap='viridis', square=True, linewidths=.5,mask=mask, cbar_kws={"shrink": .5})

            plt.title('Matrice de corrélation')
            plt.show()
            st.pyplot()
    else:
        st.warning('Aucune donnée numérique disponible. \n \n Veuillez sélectionner un traitement à appliquer sur un autre type de données.')
    if not others_table.empty:
        if opt_detail:
            st.subheader("Données non numériques")
            st.dataframe(others_table.describe())
    else:
        st.warning('Aucune donnée non numérique disponible. \n \n Veuillez sélectionner un traitement à appliquer sur un autre type de données.')
    if opt_manquant:
        st.subheader("Données manquantes")
        col1, col2 = st.beta_columns((2,1))
        col2.write(select_table.isna().sum())
        plt.figure(figsize=(5,5))
        sn.heatmap(select_table.isnull(), cbar=False)
        col1.pyplot()
    


st.write('')
    

    
