import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Título de la app
st.title("Análisis de Vehiculos")
# Cargar los datos


@st.cache_data
def cargar_datos():
    # Simulación de carga, reemplaza esto con tu CSV o fuente real
    df = pd.read_csv("vehicles_us.csv")  # Leer archivo
    return df


df = cargar_datos()
# Mostrar tabla
st.subheader("Vista previa del dataset")
st.dataframe(df.head(50))  # Muestra los primeros 50 por rendimiento

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
