import random
import time
import sys
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
    print( "="*40 + "\033[0m")  # Línea superior
    print("\033[1;36m🌟   GESTIÓN DE EXPERIMENTOS   🌟\033[0m")  # Título centrado con emoji
    print( "="*40 )  # Línea inferior

    print("1️⃣  Agregar Experimento 🧪\033[0m")  # Opción con emoji
    print("")
    print("2️⃣  Mostrar Experimentos 📋\033[0m")
    print("")
    print("3️⃣  Eliminar Experimento ❌\033[0m")
    print("")
    print("4️⃣  Salir 🚪\033[0m")

print("="*40 + "\033[0m")