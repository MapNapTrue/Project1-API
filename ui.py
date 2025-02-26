from api import obtener_datos

def iniciar_interfaz():
    print("Consulta de casos de COVID-19 en Colombia")

    # Pedir datos al usuario
    departamento = input("Ingrese el nombre del departamento: ")
    limite = int(input("Ingrese el número de registros a consultar: "))

    # Obtener datos
    datos = obtener_datos(departamento, limite)

    # Verificar si hay datos
    if datos.empty:
        print(f"No se encontraron datos para el departamento '{departamento}'.")
        return

    # Asegurar que haya suficientes registros
    if len(datos) < limite:
        print(f"⚠️ Solo se encontraron {len(datos)} registros para {departamento}.")

    # Mostrar resultados en formato tabla con format()
    print("\nResultados de la consulta:")
    print("{:<20} {:<15} {:<5} {:<20} {:<10} {:<15}".format(
        "Ciudad", "Departamento", "Edad", "Tipo", "Estado", "País de Procedencia"
    ))
    print("-" * 90)

    for _, row in datos.iterrows():
        print("{:<20} {:<15} {:<5} {:<20} {:<10} {:<15}".format(
            row["ciudad_municipio_nom"], row["departamento_nom"], row["edad"], 
            row["fuente_tipo_contagio"], row["estado"], row["pais_viajo_1_nom"]
        ))
