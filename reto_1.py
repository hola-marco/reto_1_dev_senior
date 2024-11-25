from datetime import datetime
import numpy as np  # Necesario para calcular la exponencial
import time
import sys
import os
import matplotlib.pyplot as plt


inventario=[]
"""Atributos de un experimento como: nombre,fecha,tipo y resultados numericos"""
def agregarExperimento(inventario):
    
    while True:
        # Solicitar datos básicos de la investigación
        while True:
            nombre = input("Digita nombre de la investigación: ").strip()
            tipo = input("Ingrese el tipo de experimento (Física, Química, Biología): ").strip().lower()
            if tipo in ['física', 'química', 'biología']:
                tipo = tipo.capitalize()
                break
            elif tipo!=("física","biología","química"):
                print("Tipo inválido. Por favor, elija entre Física, Química o Biología.")
                print("vueleve a intentarlo")
            else:
                print("incorrecto")
                break
        
        while True:
                
                fecha = input("Digita la fecha (d/m/a) ").strip().lower()
                try:
                    fechas= datetime.strptime(fecha, "%d/%m/%Y")  # Conversión correcta de fecha
                    break  # Salir del bucle si la fecha es válida
                except ValueError:
                    print("Fecha no válida. Debe tener el formato d/m/a (ejemplo: 25/12/2023).")
                    n=input("volver a digitar fecha s/n :")
                    if n=="n":
                     break
                    elif n!="s"and n!="n":
                     print("Error de opcion")
                     break
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
    return inventario
    
  
def visualizarExperimentos(inventario):
    
    if not inventario:
      print("El inventario está vacío. No hay investigaciones para mostrar.")
      return
    print(" "*20,"  Inventario  Experimentos ")
    for idx, inv in enumerate(inventario, start=1):
        # Mostrar resultados con saltos de línea
        resultados_str = " | ".join(map(str, inv['resultados']))
        print("="*20)
        print(f"Experimento N° {idx}",)
        print("="*20)
        print(f"Nombre: ",inv['nombre'])
        print(f"Tipo: ", inv['tipo'],)
        print(f"Fecha: ",inv['fecha'])
        print("Resultados:",resultados_str)
        print("="*20)

def calcular_estadisticas(inventario):
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

def generar_informe():
    pass
def eliminarExperimento(inventario):
    
    if not inventario:
        print("Error: El inventario está vacío.")
        return
    
    print(" " * 20, "  Inventario de Experimentos ")
    
    opcion = input("\nIngresa el nombre de la investigación que deseas eliminar: ").strip()
    
    # Buscar la investigación por nombre
    for inv in inventario:
        if inv['nombre'].lower() == opcion.lower():  # Comparación sin importar mayúsculas/minúsculas
            inventario.remove(inv)  # Eliminar la investigación
            print(f"\nLa investigación '{opcion}' ha sido eliminada exitosamente.")
            return
    
    # Si no se encuentra la investigación
    print(f"\nNo se encontró ninguna investigación con el nombre '{opcion}'.")

        
        
def mostar_menu():
  
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        RESET = "\033[0m"
        negro = "\033[30m"

        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        # Definir los códigos de colores ANSI para Azul, Negro y Blanco
        # Definir los códigos de colores ANSI para azul rey
        azul_rey = "\033[38;5;33m"  # Azul rey (256 colores)
        reset = "\033[0m"  # Reset para restaurar el color original

        print(GREEN," "*30,"        +--------------------------+")
        print(GREEN," "*30,"       /|",  azul_rey , "DEV     🐍💻",GREEN,"         /|")
        print(GREEN," "*30,"      / |  ",negro ,"   SENIOR  ",GREEN,"       / |")
        print(GREEN," "*30,"     /  |      ", RESET,"     CODE ",GREEN,"   /  |")
        print(GREEN," "*30,"    +--------------------------+   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  |   ██████████████████  |   |")
        print(GREEN," "*30,"    |  |   |",RESET,"MENU PRINCIPAL ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🧪 | ",RESET,"1. Gestión de ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Experimentos ",GREEN," |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🔍 | ",RESET,"2. Análisis de",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Datos        ",GREEN," |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |📊 |",RESET,"3.Generación   ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Informe    ",GREEN,"   |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🔙 |",RESET,"4. Salir    ",GREEN,"   |   |")
        print(GREEN," "*30,"    |  |   +-------------------+   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  +-----------------------|   |")
        print(GREEN," "*30,"    +-------------------------+|")
        print(GREEN," "*30,"    |/                         |/")
        print(GREEN," "*30,"    +---------------------------+",RESET)
def subMenu():
    print(" "*40, "="*40 + "\033[0m")  # Línea superior
    print(" "*40,"\033[1;36m🌟   GESTIÓN DE EXPERIMENTOS   🌟\033[0m")  # Título centrado con emoji
    print( " "*40,"="*40 )  # Línea inferior

    print(" "*40,"1️⃣  Agregar Experimento 🧪\033[0m")  # Opción con emoji
    print("")
    print(" "*40,"2️⃣  Mostrar Experimentos 📋\033[0m")
    print("")
    print(" "*40,"3️⃣  Eliminar Experimento ❌\033[0m")
    print("")
    print(" "*40,"4️⃣  Salir 🚪\033[0m")

    print(" "*40,"="*40 + "\033[0m")
def main():
     while True:
        mostar_menu()
        print(" "*15,"="*20)
        opcion=input("                Digita opcion:")
        print(" "*15,"="*20)
        os.system('cls')
        if opcion=="1":
            while True:
                subMenu()
                option=input("           Digita opcion:")
                os.system('cls')
                if option=="1":
                    agregarExperimento(inventario)
                 
                elif option=="2":
                    visualizarExperimentos(inventario)
                elif option=="3":
                    eliminarExperimento(inventario)
                else:
                    print("  OPcion invalida:")
                    break
                
        elif opcion=="2":
           calcular_estadisticas(inventario)
        elif opcion=="3":
             generar_informe(inventario)
        elif opcion=="4":
            print("Saliendo de programa")
            break
        else:
            print("Opcion Invalida ")
            input()
             
    
main()