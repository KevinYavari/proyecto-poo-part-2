import requests
import json
import streamlit as st

def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data[0]
    else:
        return None

def show_country_info(country_data):
    if country_data is not None:
        st.write(f"Nombre del país: {country_data.get('name', 'No disponible')}")

        # Acceder a la lista de capitales de manera segura
        capitals = country_data.get('capital', [])
        capital = capitals[0] if capitals else 'No disponible'
        st.write(f"Capital: {capital}")

        # Acceder a la lista de 'currencies' de manera segura
        currencies_info = country_data.get('currencies', {})
        moneda = currencies_info.get('COP', {}).get('name', 'No disponible')
        st.write(f"Moneda: {moneda}")

        st.write(f"Región: {country_data.get('region', 'No disponible')}")
        st.write(f"Subregión: {country_data.get('subregion', 'No disponible')}")
        st.write(f"Población: {country_data.get('population', 'No disponible')}")

        # Mostrar la bandera
        bandera_url = country_data.get('flags', {}).get('png', 'No disponible')
        st.image(bandera_url, caption='Bandera', use_column_width=True)
    else:
        st.error("Error al obtener la información del país. Verifica el nombre e inténtalo de nuevo.")

def main():
    st.title("Información de Países")
    nombre_pais = st.text_input("Ingrese el nombre del país:")
    if st.button("Buscar"):
        country_data = get_country_data(nombre_pais)
        show_country_info(country_data)

if __name__ == "__main__":
    main()
