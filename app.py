import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px 

apgn = pd.read_csv('datos_anteproyecto.csv') #apgn = df
ran = pd.read_csv('datos_random.csv') # df2 = ran

st.title("Aplicación 2")

tab1, tab2 = st.tabs(['Tab 1' , 'Tab 2'])

with tab1:
    # análisis univariado, mirar como se distribuye cada variable
    fig, ax = plt.subplots(1, 3, figsize = (10, 4)) # Espacio a graficar, una fila con 3 columnas

    # educ - grafico de barras
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values, color = "purple")

    # sexo - histograma
    ax[1].hist(ran['edad'], bins = 30, color = "yellow")

    # wage
    ax[2].hist(ran['wage'], bins = 40, color = "pink")

    st.pyplot(fig)

    # análisis bivariado
    fig, ax = plt.subplots(1, 2, figsize = (10, 4))

    # educ vs. wage
    ax[0].scatter(ran['educ'], ran['wage'], color = "green")

    # edad vs. wage
    ax[1].scatter(ran['edad'], ran['wage'], color = "blue") 

    st.pyplot(fig)

with tab2:
    fig = px.treemap(data_frame=apgn,
           path = [px.Constant("PGN"),
                   "Nombre Sector",
                   "Tipo de gasto"],
           values = 'Valor', color = "Nombre Sector", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig)