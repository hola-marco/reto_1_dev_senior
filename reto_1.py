from datetime import datetime
import numpy as np  # Necesario para calcular la exponencial
import time
import sys
import os
import matplotlib.pyplot as plt
import statistics


inventario=[]
"""Atributos de un experimento como: nombre,fecha,tipo y resultados numericos"""
def agregarExperimento(inventario):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    detener = "\033[0m"
    negro = "\033[30m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"    
    while True:
        # Solicitar datos básicos de la investigación
        
        while True:
            nombre = input("Digita nombre de la investigación: ").strip()
            tipo = input("Ingrese el tipo de experimento (Física, Química, Biología): ").strip().lower()
            if tipo in ['fìsica', 'quìmica', 'biologìa']:
                tipo = tipo.capitalize()
                break
            
            else:
                print("incorrecto")
                
                
        
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
                resultado = int(input("Digita un resultado de la investigación (escribe 'fin' para terminar): "))
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
        print("No hay datos suficientes para realizar el análisis. El inventario está vacío.")
        return  # Salir si no hay inventario

    for idx, inv in enumerate(inventario, start=1):
        cantidad_resultados = len(inv["resultados"])
        if cantidad_resultados < 3:
            print(f"La investigación '{inv['nombre']}' no tiene suficientes resultados para analizar (mínimo: 3).")
        else:
            print(f"La investigación '{inv['nombre']}' tiene {cantidad_resultados} resultados, lista para análisis.")

    
    for inven in inventario:
        promedio=statistics.mean(inven["resultados"])
        maximo=max(inven["resultados"])
        minimo=min(inven["resultados"])
        print(f" Analisis de experimento {inven["nombre"]}")
        print(f" Promedio de resultados {promedio}")
        print(f"maximo de resultados {maximo}")
        print(f"Minimo de resultados  {minimo}")
        print("="*20)
    # Organizar datos
    fechas = []
    resultado = []
    nombres = []

    for elemento in inventario:
        # Convertir fecha a formato datetime
        fechas.append(datetime.strptime(elemento["fecha"], "%d/%m/%Y"))
        resultado.append(elemento["resultados"])
        nombres.append(elemento["nombre"])

    print("="*20)
    print("Ahora podemos dar un analisis mediante un grafico")
    print("Selecciona el tipo de gráfico:")
    print("="*20)
    print(" ")
    print("1. Gráfico de líneas")
    print(" ")
    print("2. Gráfico de barras")
    print(" ")
    print("3. Gráfico de dispersión")
    opcion = input("Digita Opcion ").strip()

    # Configuración inicial del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    if opcion == "1":
        # Gráfico de líneas
        for i, res in enumerate(resultado):
            ax.plot(
                [fechas[i]] * len(res),
                res,
                marker="o",
                label=nombres[i]
            )
        ax.set_title("DEV SENIOR CODE", fontsize=14)
        ax.set_title("Gráfico de Líneas: Resultados de Investigaciones", fontsize=14)


    elif opcion == "2":
        # Gráfico de barras
        for i, res in enumerate(resultado):
            ax.bar(
                [fechas[i] + np.timedelta64(idx, 'D') for idx in range(len(res))], 
                res,
                label=nombres[i],
                alpha=0.7
            )
        ax.set_title("Gráfico de Barras: Resultados de Investigaciones", fontsize=14)

    elif opcion == "3":
        # Gráfico de dispersión
        for i, res in enumerate(resultado):
            ax.scatter(
                [fechas[i]] * len(res),
                res,
                label=nombres[i]
            )
        ax.set_title("Gráfico de Dispersión: Resultados de Investigaciones", fontsize=14)
    
    else:
        print("Opción inválida.")
        return

    # Configurar los ejes y personalización
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Resultados", fontsize=12)
    ax.legend(title="Investigación", fontsize=10)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    # Mostrar el gráfico
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
        print(" "*35,"\033[38;5;33m="*28,"\033[0m")
        opcion=input("                                     Digita opcion:")
        print(" "*35,"\033[38;5;33m="*25,"\033[0m")
        time.sleep(2)
        os.system('cls')
        if opcion=="1":
            while True:
                subMenu()
                option=input("                                          Digita opcion:")
                os.system('cls')      
                if option=="1":
                    agregarExperimento(inventario)
                    
                    input("Digita Enter para continuar")
                    
                    os.system('cls')
                    print(" "*30,"="*30)
                    print("                             VOLVIENDO  A GESTION  DE EXPERIMENTOS")
                    print(" "*30,"="*30)
                    time.sleep(2)
                    os.system('cls')
    
                elif option=="2":
                    visualizarExperimentos(inventario)
                    input("Digita Enter para continuar")
                   # os.system('cls')
                elif option=="3":
                    eliminarExperimento(inventario)
                    input("Digita Enter para continuar")
                    os.system('cls')
                else:
                    print("  OPcion invalida:")
                    time.sleep(2)
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
            
             
    
main()