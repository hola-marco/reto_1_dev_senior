import matplotlib.pyplot as plt
from datetime import datetime

# Lista de diccionarios con datos
datos = [
    {"nombre": "investigacion ", "fecha": "2023-01-01", "tipo": "Física", "resultados": [5, 9, 5]},
    {"nombre": "Estudio B", "fecha": "2023-02-01", "tipo": "Física", "resultados": [9, 8, 6]},
    {"nombre": "Estudio C", "fecha": "2023-03-01", "tipo": "Física", "resultados": [88, 91, 90]},
    {"nombre": "Estudio D", "fecha": "2023-01-01", "tipo": "Química", "resultados": [75, 77, 76]},
    {"nombre": "Estudio E", "fecha": "2023-02-01", "tipo": "Química", "resultados": [80, 82, 81]},
    {"nombre": "Estudio F", "fecha": "2023-03-01", "tipo": "Química", "resultados": [78, 79, 77]},
    {"nombre": "Estudio G", "fecha": "2023-01-01", "tipo": "Biología", "resultados": [70, 68, 69]},
    {"nombre": "Estudio H", "fecha": "2023-02-01", "tipo": "Biología", "resultados": [65, 66, 67]},
    {"nombre": "Estudio I", "fecha": "2023-03-01", "tipo": "Biología", "resultados": [68, 70, 69]},
]

# Organizar datos por tipo
series = {}
for punto in datos:
    tipo = punto["tipo"]
    if tipo not in series:
        series[tipo] = {"fechas": [], "promedios": [], "nombres": []}
    # Agregar datos a la serie correspondiente
    series[tipo]["fechas"].append(datetime.strptime(punto["fecha"], "%Y-%m-%d"))
    promedio = sum(punto["resultados"]) / len(punto["resultados"])
    series[tipo]["promedios"].append(promedio)
    series[tipo]["nombres"].append(punto["nombre"])

# Crear gráfica de líneas
plt.figure(figsize=(12, 8))
for tipo, valores in series.items():
    plt.plot(
        valores["fechas"],
        valores["promedios"],
        marker="o",
        label=f"{tipo}",
        linewidth=2
    )
    # Añadir etiquetas con los nombres de las investigaciones
    for i in range(len(valores["fechas"])):
        plt.text(
            valores["fechas"][i],
            valores["promedios"][i] + 1,
            valores["nombres"][i],
            fontsize=9,
            ha="center"
        )

# Configuración de la gráfica
plt.title("Resultados de Investigaciones por Tipo (Gráfica de Líneas)", fontsize=14)
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Promedio de Resultados", fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 100)  # Escala del eje Y
plt.legend(title="Tipo de Investigación", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
