import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np  # Necesario para calcular la exponencial

inventario = []

def agregar(inventario):
    
    while True:
        # Solicitar datos básicos de la investigación
        while True:
            nombre = input("Digita nombre de la investigación: ").strip()
            tipo = input("Ingrese el tipo de experimento (Física, Química, Biología): ").strip().lower()
            if tipo in ['física', 'química', 'biología']:
                tipo = tipo.capitalize()
                
            elif tipo!=("física","biología","química"):
                print("Tipo inválido. Por favor, elija entre Física, Química o Biología.")
                print("vueleve a intentarlo")
            break
        while True:
                
                fecha = input("Digita la fecha (d/m/a) ").strip().lower()
                try:
                    fechas = datetime.strptime(fecha, "%d/%m/%Y")  # Conversión correcta de fecha
                    break  # Salir del bucle si la fecha es válida
                except ValueError:
                    print("Fecha no válida. Debe tener el formato d/m/a (ejemplo: 25/12/2023).")
                    n=input("digita s/n")
                    if n=="s":
                     break
                    elif n!="s"and n!="n":
                     print("Error de opcion")
                op=input("quieres seguir agregando investigaciones s/n")  
                if op=="n":
                 break   
        resultados = []
        while True:
            try:
                resultado = float(input("Digita un resultado de la investigación (escribe 'fin' para terminar): "))
                resultados.append(resultado)  # Agregar resultado a la lista
            except ValueError:
                finalizar = input("¿Terminar ingreso de resultados? (s/n): ").strip().lower()
                if finalizar == "s":
                    break

        investigacion = {
            "nombre": nombre,
            "tipo": tipo,
            "fecha": fecha,
            "resultados": resultados
        }
        
        inventario.append(investigacion)
        
        continuar = input("¿Deseas agregar otra investigación? (s/n): ").strip().lower()
        if continuar != "s":
            break
    

def analisi(inventario):
    if not inventario:
        print("No hay datos en el inventario para analizar.")
        return

    fechas = []
    resultados_exponenciales = []

    # Diccionarios para almacenar datos procesados
    fecha_diccionario = {}
    resultados_diccionario = {}

    # Organizar los datos
    for idx, elemento in enumerate(inventario):
        fecha_diccionario[f"Estudio_{idx + 1}"] = elemento["fecha"]
        resultados_diccionario[f"Estudio_{idx + 1}"] = elemento["resultados"]
        
        # Convertir fechas a formato datetime
        fechas.append(datetime.strptime(elemento["fecha"], "%d/%m/%Y"))

        # Calcular los resultados exponenciales
        resultados_exponenciales.append(np.exp(elemento["resultados"]))

    # Mostrar datos organizados
    print("\nFechas por investigación:", fecha_diccionario)
    print("\nResultados por investigación:", resultados_diccionario)

    # Graficar
    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, inv in enumerate(inventario):
        ax.plot(
            [fechas[idx]] * len(inv["resultados"]),  # Fecha repetida para cada resultado
            np.exp(inv["resultados"]),  # Resultados exponenciales
            marker="o",
            label=inv["nombre"]
        )

    # Personalización del gráfico
    ax.set_title("Resultados Exponenciales de Investigaciones", fontsize=14)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Resultados Exponenciales", fontsize=12)
    ax.legend(title="Investigación", fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

        
while True:
    op=input("digita opcion")
    if op=="1":
        agregar(inventario)
    elif op=="2":
        analisi(inventario)
            


                

            


            



