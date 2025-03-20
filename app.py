import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos con ruta relativa
car_data = pd.read_csv("vehicles_us.csv")

# Título de la aplicación
st.title('Análisis de Datos de Anuncios de Venta de Vehículos')

# Botones para mostrar/ocultar gráficos
show_hist = st.checkbox(" Mostrar Histograma", value=True)
show_scatter = st.checkbox("Mostrar Gráfico de Dispersión", value=True)

# Histograma
if show_hist:
    with st.expander(" Histograma de Odómetro"):
        st.write("Distribución de kilometraje en los anuncios de venta de coches")
        fig_hist = px.histogram(
            car_data, x="odometer",
            color_discrete_sequence=["#FF5733"],  # Color personalizado
            title="Distribución del Odómetro en Vehículos"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if show_scatter:
    with st.expander(" Gráfico de Dispersión Precio vs. Odómetro"):
        st.write("Relación entre kilometraje y precio de los vehículos")
        fig_scatter = px.scatter(
            car_data, x="odometer", y="price",
            color="price",  # Colorear por precio
            color_continuous_scale="Viridis",  # Paleta de colores
            title="Relación entre Odómetro y Precio"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
