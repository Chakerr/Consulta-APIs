# Ejercicios de Consulta a APIs Públicas

Este repositorio contiene ejercicios de programación en Python que realizan consultas a diferentes **APIs públicas** para obtener y procesar información.

## Contenido

### 1. Consulta a la PokéAPI
- **Archivo:** `pokemon_api.py`
- **Descripción:** Este script consulta la **PokéAPI** para obtener datos sobre el Pokémon `Toxel`, incluyendo su nombre, altura y peso.
- **API utilizada:** [PokéAPI](https://pokeapi.co/)
- **Ejemplo de salida:**
  ```
  Información del Pokémon:
  Nombre: toxel
  Altura: 4
  Peso: 110
  ```

### 2. Consulta a la API del Banco Mundial
- **Archivo:** `worldbank_api.py`
- **Descripción:** Este script consulta la API del **Banco Mundial** para obtener la tasa de alfabetización de varios países de América Latina.
- **API utilizada:** [World Bank API](https://data.worldbank.org/)
- **Ejemplo de salida:**
  ```
  País: Colombia
  Año: 2020
  Tasa de alfabetización: 95.2
  ------------------------------
  ```

## Tecnologías utilizadas
- **Lenguaje:** Python  
- **Librerías:** requests

## Cómo ejecutar los scripts
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Chakerr/Consulta-APIs.git
   cd ejercicios-consulta-apis
   ```
2. Instala Python 3 y pip si no los tienes:
   ```bash
   # Para Debian/Ubuntu
   sudo apt update && sudo apt install python3 python3-pip
   ```
3. Instala la librería requests:
   ```bash
   pip install requests
   ```
4. Ejecuta el script deseado:
   ```bash
   python3 pokemon_api.py
   ```
   o
   ```bash
   python3 worldbank_api.py
   ```
