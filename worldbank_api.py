import requests

def obtener_datos_educacion():
    url = "http://api.worldbank.org/v2/country/BR;AR;CO;MX;CL/indicator/SE.ADT.LITR.ZS?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        if len(datos) > 1 and isinstance(datos[1], list):  # Verificar que haya datos válidos
            for registro in datos[1]:
                pais = registro.get('country', {}).get('value', 'Desconocido')
                anio = registro.get('date', 'Desconocido')
                tasa = registro.get('value', 'No disponible')

                print(f"País: {pais}")
                print(f"Año: {anio}")
                print(f"Tasa de alfabetización: {tasa}")
                print("-" * 30)
    else:
        print(f"Error al obtener los datos. Código de estado: {response.status_code}")

if __name__ == "__main__":
    obtener_datos_educacion()
