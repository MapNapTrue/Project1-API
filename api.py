import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite):
    APP_TOKEN = "IXXfopWrgd9kHBA5DSXKE8e4D"  # Reemplázalo por tu token real
    client = Socrata("www.datos.gov.co", APP_TOKEN)

    # Obtener datos SIN FILTRO y con un límite mayor para asegurar registros suficientes
    results = client.get("gt2j-8ykr", limit=limite * 100)

    # Convertir resultados a DataFrame
    results_df = pd.DataFrame.from_records(results)

    # Verificar que haya datos
    if results_df.empty:
        print(f"⚠️ No se encontraron datos en la API para '{departamento}'.")
        return pd.DataFrame()

    # Filtrar solo los registros que pertenecen al departamento consultado
    if "departamento_nom" in results_df.columns:
        results_df = results_df[results_df["departamento_nom"].str.upper() == departamento.upper()]

    # Definir las columnas requeridas
    columnas_necesarias = ["ciudad_municipio_nom", "departamento_nom", "edad",
                            "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]

    # Verificar qué columnas existen realmente en los datos
    columnas_existentes = [col for col in columnas_necesarias if col in results_df.columns]

    # Filtrar solo las columnas disponibles
    results_df = results_df[columnas_existentes]

    # Si la columna "pais_viajo_1_nom" no existe, crearla con "Colombia"
    if "pais_viajo_1_nom" not in results_df.columns:
        results_df["pais_viajo_1_nom"] = "Colombia"
    else:
        # Reemplazar valores nulos por "Colombia"
        results_df["pais_viajo_1_nom"] = results_df["pais_viajo_1_nom"].fillna("Colombia")

    # Limitar la cantidad de registros finales
    results_df = results_df.head(limite)

    return results_df
