import requests

# Lista de países latinoamericanos con su código en la API del Banco Mundial
paises = ["ARG", "BRA", "COL", "MEX", "PER", "CHL"]

# Indicador: Tasa bruta de matrícula en educación primaria
indicador = "SE.PRM.ENRR"

print("\nTasa Bruta de Matrícula en Educación Primaria por País en Latinoamérica\n")

for pais in paises:
    URL = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json&per_page=5"
    respuesta = requests.get(URL)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        if len(datos) > 1 and datos[1]:
            encontrado = False  # Bandera para verificar si hay datos válidos
            for entrada in datos[1]:  # Recorremos varios años para encontrar datos disponibles
                nombre_pais = entrada["country"]["value"]
                anio = entrada["date"]
                valor = entrada["value"]

                if valor:  # Si encontramos un dato válido, lo imprimimos
                    print(f"País: {nombre_pais}")
                    print(f"Año: {anio}")
                    print(f"Tasa de matrícula: {valor}%")
                    print("-" * 60)
                    encontrado = True
                    break  # Nos quedamos con el dato más reciente disponible
            
            if not encontrado:
                print(f"No hay datos recientes para {nombre_pais}")

    else:
        print(f"Error al obtener datos para {pais}")

