import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos con ruta relativa
car_data = pd.read_csv("vehicles_us.csv")


# Título de la aplicación
st.title('Análisis de Datos de Anuncios de Venta de Vehículos')
st.markdown("""
### 🛠️ Detalles del Proyecto
En este proyecto se realizara un analisis preliminar de datos del conjunto `vehicles_us` este dataframe incluye datos sobre kilometraje, precio, modelo, etc.
- **Datos:** Vehículos en venta en EE.UU.
- **Objetivo:** Analizar la relación entre odómetro y precio.
- 🔍 *Usamos gráficos interactivos con Plotly.*
""")

st.header("Exploración de datos")
st.dataframe(car_data)

st.subheader("Filtrar por año de fabricación:")
st.markdown("""Como analista de datos, se puede realizar un filtrado de los datos utilizando la columna `model_year` para segmentar los vehículos según su año de modelo. Este enfoque permite identificar patrones de comportamiento de compra de los consumidores, analizando tendencias y preferencias asociadas a vehículos de diferentes años.""")

selected_year = st.selectbox("Selecciona un año:", sorted(
    car_data['model_year'].dropna().unique().astype(int)))

# Filtrar datos por el año seleccionado
filtered_data = car_data[car_data['model_year'] == selected_year]

# Mostrar la tabla filtrada
st.dataframe(filtered_data)

st.header("Distribucion Grafica basado en el Odometro de los Vehiculos")
st.markdown(""" - Se puede seleccionar y visualizar la distribución gráfica de los precios de los vehículos en función de su kilometraje (odómetro), lo que permitirá identificar patrones, tendencias y relaciones entre estas dos variables clave.""")

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

st.header("Next Analysis")
st.subheader("To be Continue")
