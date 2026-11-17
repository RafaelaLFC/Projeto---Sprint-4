import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Análise de Anúncios de Venda de Veículos')
st.write('Use as caixas de seleção abaixo para explorar os dados de anúncios de carros nos EUA.')


build_histograma = st.checkbox('Criar um histograma')

if build_histograma: 
    st.write('Criando um histograma para a coluna odometer')
    
  
    fig = px.histogram(car_data, x="odometer")

    
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter: 
    
    st.write('Criando um gráfico de dispersão: odometer x price')

    
    fig = px.scatter(car_data, x="odometer", y="price")

    
    st.plotly_chart(fig, use_container_width=True)
