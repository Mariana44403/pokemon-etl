import requests
import pandas as pd
import psycopg2

def extract(poke_ids):
    data = []
    for poke_id in poke_ids:
        url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            poke = response.json()
            data.append({
                "id": poke["id"],
                "nombre": poke["name"],
                "altura": poke["height"],
                "ancho": poke["weight"],
                "experiencia_base": poke["base_experience"]
            })
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de {url}: {e}")
            continue
    
    return pd.DataFrame(data)    

def transform(df):
    df["peso_kg"] = df["ancho"] / 10
    return df[df["experiencia_base"] > 100].sort_values("experiencia_base", ascending=False)

def load(df):
    conn = psycopg2.connect(
        dbname="etl_practica",
        user="nombre",
        password="12345",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO pokemon (id, nombre, altura, ancho, experiencia_base, peso_kg)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (row["id"], row["nombre"], row["altura"], row["ancho"], row["experiencia_base"], row["peso_kg"]))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__": 
    df_raw = extract([6, 7, 8, 9, 10])
    print("Datos extraídos:")
    print(df_raw)

    df_clean = transform(df_raw)
    print("\nDatos transformados:")
    print(df_clean)

    load(df_clean)
    print("\nDatos cargados exitosamente en la base de datos.")
