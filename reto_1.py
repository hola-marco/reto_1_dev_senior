import datetime
import random
import time
import sys
import os
inventario=[]
"""Atributos de un experimento como: nombre,fecha,tipo y resultados numericos"""
def agregar_experimento():
     print("Agregando nuevo experimento")
     print("")
     nombre = input("Ingrese el nombre del experimento: ")
     fecha = input("Ingrese la fecha de realización (YYYY-MM-DD): ")
    
     while True:
        tipo = input("Ingrese el tipo de experimento (Física, Química, Biología): ").strip().lower()
        if tipo in ['física', 'química', 'biología']:
            tipo = tipo.capitalize()
            break
        else:
            print("Tipo inválido. Por favor, elija entre Física, Química o Biología.")
    
     resultados = input("Ingrese los resultados obtenidos: ")
    
    # Agregar el experimento a la lista
     inventario.append({
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados
     })
     input("Digita enter para continuar")
     os.system('cls')

# Uso del código
     return inventario


    




    
def visualizar_experimentos():
    global inventario
    if not inventario:
        print("EL inventario de experimentos se encuentra vacio:")
    else:
        print(" "*30,"="*70)
        print(" "*30,"           INVENTARIO DE EXPERIMENTOS  ")

        print(" "*30,"="*70)
        print(f"{" "*31}{'Nombre':<20} {'Fecha':<15} {'Tipo':<10} {'Resultados':<10}")
        print(" "*30,"="*70)  # Línea de separación

        for experimento in inventario:
            nombre = experimento["nombre"]
            fecha = experimento["fecha"]
            tipo = experimento["tipo"]
            resultados = experimento["resultados"]
            
            # Mostrar cada experimento de forma ordenada
            print(f"{" "*31}{nombre:<20} {fecha:<15} {tipo:<10} {resultados:<10}")
            input("                               ======= DIgita enter para continuar ==== ")
            os.system('cls')



def calcular_estadisticas():
    pass
def comparar_experimentos():
    pass
def generar_informe():
    pass
def eliminarExperimento():
        pass
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
def menuexperimentos():
    print(" "*40,"=" * 20)
    print(" "*40,"      🧪 MENÚ DE EXPERIMENTOS 🧪")
    print(" "*40,"=" * 20)
    print(" "*40,"1️⃣ Física ⚡")
    print(" "*40,"2️⃣ Química 🧫")
    print(" "*40,"3️⃣ Biología 🌱")
    print(" "*40,"4️⃣ Salir 🚪")
    print(" "*40,"=" * 20)

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
                    agregar_experimento()
                 
                elif option=="2":
                    visualizar_experimentos()
                elif option=="3":
                    eliminarExperimento()
                else:
                    print("  OPcion invalida:")
                    break
                
        elif opcion=="2":
           calcular_estadisticas()
        elif opcion=="3":
             generar_informe()
        elif opcion=="4":
            print("Saliendo de programa")
            break
        else:
            print("Opcion Invalida ")
            input()
             
    
main()