inventario = []

while True:
    # Solicitar datos básicos de la investigación
    nombre = input("Digita nombre de la investigación: ").strip()
    tipo = input("Digita el tipo de investigación: ").strip()
    fecha = input("Digita la fecha (d/m/a): ").strip()
    
    # Crear un diccionario para almacenar los resultados
    resultados = []
    while True:
        try:
            resultado = float(input("Digita un resultado de la investigación (escribe 'fin' para terminar): "))
            resultados.append(resultado)  # Agregar resultado a la lista
        except ValueError:
            # Finalizar ingreso de resultados al escribir "fin"
            finalizar = input("¿Terminar ingreso de resultados? (s/n): ").strip().lower()
            if finalizar == "s":
                break

    # Crear un diccionario con la información de la investigación
    investigacion = {
        "nombre": nombre,
        "tipo": tipo,
        "fecha": fecha,
        "resultados": resultados
    }
    
    # Agregar el diccionario al inventario
    inventario.append(investigacion)
    
    # Preguntar si se desea agregar otra investigación
    continuar = input("¿Deseas agregar otra investigación? (s/n): ").strip().lower()
    if continuar != "s":
        break

# Mostrar los datos almacenados en el inventario
print("\n=== Inventario de Investigaciones ===")
for idx, ins in enumerate(inventario, start=1):
    print(f"Investigación {idx}:")
    print(f"  Nombre: {ins['nombre']}")
    print(f"  Tipo: {ins['tipo']}")
    print(f"  Fecha: {ins['fecha']}")
    print(f"  Resultados: {ins['resultados']}")
    print()
