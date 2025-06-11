import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scat_button = st.button('Construir Gráfico de Dispersión')
if scat_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir Histograma')
build_scatter = st.checkbox('Construir Gráfico de Dispersión')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
if build_scatter:
    st.write('Construir un gráfico de dispersión para la columna odómetro')
    fig = px.scatter(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

