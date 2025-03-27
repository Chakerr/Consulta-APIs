import requests

def main():
    # URL de la PokéAPI para obtener datos de Pikachu
    url = "https://pokeapi.co/api/v2/pokemon/toxel"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parseamos la respuesta como JSON
        print("Información del Pokémon:")
        print("Nombre:", data["name"])
        print("Altura:", data["height"])
        print("Peso:", data["weight"])
        # Puede extraer más campos de la API
    else:
        print("Error al obtener los datos. Código de estado:", response.status_code)

if __name__ == "__main__":
    main()