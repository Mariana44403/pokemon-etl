## pokemon-etl
Este proyecto es una práctica de pipeline ETL (Extract, Transform, Load) utilizando Python.

## Objetivo
Practicar conceptos fundamentales de ingeniería de datos:

- Extracción desde una API pública
- Transformación de datos con pandas
- Cargar en una base de datos relacional
- Modularización del código en funciones extract, transform y load

## Tecnologías utilizadas
- Python 3
- Pandas
- Requests
- PostgreSQL
- psycopg2

## Como ejecutar el proyecto
1. Clona el repositorio git clone https://github.com/Mariana44403/etl-pokemon.git cd etl-pokemon
2. Crear un entorno virtual y activarlo 
    python -m venv venv source venv/bin/activate # En Ubuntu
3. Instala las dependencias 
    pip install -r requirements.txt
4. Tener una base de datos PostgreSQL creada, con una tabla llamada pokemon, con esta estructura        
    CREATE TABLE pokemon ( 
        id INT PRIMARY KEY, 
        nombre TEXT, 
        altura INT, 
        ancho INT, 
        experiencia_base INT, 
        peso_kg FLOAT 
    );

5. Ejecuta el pipeline 
    python3 etl.py

## Requisitos previos
- Tener PostgreSQL instalado y corriendo
