import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
inventario= []
while True:
    nombre=input("Digita nombre de investigacion : ")
    tipo=input("Digita el tipo de investigacion:")
    fecha=input("digita fecha d/m/a :")
    while True:
      resultados=input("digita los resultados de la investigacion")
      

    categorias = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
    valores1 = [25, 30, 35, 40, 50]  # Resultado 1
    valores2 = [20, 40, 55, 60, 70]  # Resultado 2
    valores3 = [30, 45, 50, 65, 80]  # Resultado 3



    # 2. Gráfico de líneas (agregando tres conjuntos de resultados)
    plt.subplot(232)  # Subgráfico 2 (2 filas, 3 columnas, subgráfico 2)
    plt.plot(categorias, valores1, label='Resultado 1', color='blue', marker='o')
    plt.plot(categorias, valores2, label='Resultado 2', color='green', marker='x')
    plt.plot(categorias, valores3, label='Resultado 3', color='orange', marker='^')
    plt.title('Gráfico de Líneas')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.legend()

# 3. Gráfico circular (pastel) para cada conjunto de resultados
plt.subplot(233)  # Subgráfico 3 (2 filas, 3 columnas, subgráfico 3)
plt.pie(valores1, labels=categorias, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Gráfico Circular (Resultado 1)')

# 4. Histograma (usando tres distribuciones de datos aleatorios para simular tres resultados)
plt.subplot(234)  # Subgráfico 4 (2 filas, 3 columnas, subgráfico 4)
np.random.seed(0)
data1 = np.random.normal(0, 1, 1000)  # Datos aleatorios para el resultado 1
data2 = np.random.normal(0, 1.5, 1000)  # Datos aleatorios para el resultado 2
data3 = np.random.normal(0, 2, 1000)  # Datos aleatorios para el resultado 3

plt.hist(data1, bins=30, alpha=0.5, label='Resultado 1', color='blue', edgecolor='black')
plt.hist(data2, bins=30, alpha=0.5, label='Resultado 2', color='green', edgecolor='black')
plt.hist(data3, bins=30, alpha=0.5, label='Resultado 3', color='orange', edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()

# 5. Gráfico de dispersión (scatter) con tres conjuntos de resultados
plt.subplot(235)  # Subgráfico 5 (2 filas, 3 columnas, subgráfico 5)
x1 = np.random.rand(50)
y1 = np.random.rand(50)

x2 = np.random.rand(50)
y2 = np.random.rand(50)

x3 = np.random.rand(50)
y3 = np.random.rand(50)

plt.scatter(x1, y1, color='blue', label='Resultado 1', alpha=0.6)
plt.scatter(x2, y2, color='green', label='Resultado 2', alpha=0.6)
plt.scatter(x3, y3, color='orange', label='Resultado 3', alpha=0.6)
plt.title('Gráfico de Dispersión')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Ajuste de disposición para que no se sobrepongan los gráficos
plt.tight_layout()

# Mostrar todos los gráficos
plt.show()