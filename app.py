import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv(
    "/Users/ASUS/Documents/Tripleten/Proyecto spring 7/Project-Vehicles/vehicles_us.csv")

st.header('Data Vehicles')

hist_button = st.button('Construir histograma')
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
