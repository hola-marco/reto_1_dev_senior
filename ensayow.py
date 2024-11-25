import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np  # Necesario para calcular la exponencial

inventario = []

# Recopilar datos
while True:
    nombre = input("Digita nombre de la investigación: ").strip()
    tipo = input("Digita el tipo de investigación: ").strip()
    fecha = input("Digita la fecha (d/m/a): ").strip()
    
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

# Organizar los datos para graficarlos
fig, ax = plt.subplots(figsize=(10, 6))

for idx, inv in enumerate(inventario, start=1):
    # Convertir la fecha en datetime
    fecha = datetime.strptime(inv["fecha"], "%d/%m/%Y")
    # Transformar los resultados usando una función exponencial
    # Aquí se aplica e^x para cada valor de los resultados.
    resultados_exponenciales = np.exp(np.array(inv["resultados"]))  # np.exp aplica la función exponencial
    
    # Graficar los resultados exponenciales
    ax.plot([fecha] * len(inv["resultados"]), resultados_exponenciales, marker="o", label=inv["nombre"])

# Personalizar el gráfico
ax.set_title("Resultados Exponenciales de Investigaciones", fontsize=14)
ax.set_xlabel("Fecha", fontsize=12)
ax.set_ylabel("Resultados Exponenciales", fontsize=12)
ax.legend(title="Investigación", fontsize=10)

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
