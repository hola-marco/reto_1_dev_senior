import matplotlib.pyplot as plt
from datetime import datetime
class Tarea:
     def __init__(self,nombre,tipos,fecha,resultados):
          self.nombre=nombre
          self.fecha=fecha
          self.tipo=tipos
          self.resultado=resultados
          

inventario = []
def agregar(inventario):
    n=True
    while True:
 
    # Solicitar datos básicos de la investigación
        nombre = input("Digita nombre de la investigación: ").strip()
        tipo = input("Digita el tipo de investigación: ").strip()
        while True:
          fecha = input("Digita la fecha (d/m/a): ").strip()
        
          try:
             fechas=datetime.strptime(fecha,"%d%m%Y")
          except ValueError:
                print("fecha no valida ")
                finalizar = input("¿volver a digitar fecha (d/m/a ? (s/n): ").strip().lower()
                if finalizar == "s":
                 break
        n=input("salir de investigacio:")
        if finalizar == "s":
         break
                   
         
                  
                
       



                 
                
                
                
            
    
    """# Crear un diccionario para almacenar los resultados
        resultados = []

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
    
    # Preguntar si se desea agregar otra investigación  continuar = input("¿Deseas agregar otra investigación? (s/n): ").strip().lower()
    if continuar != "s":
    break

# Organizar los datos para graficarlos
fig, ax = plt.subplots(figsize=(10, 6))

for idx, inv in enumerate(inventario, start=1):
    # Convertir la fecha a formato datetime
    fecha = datetime.strptime(inv["fecha"], "%d/%m/%Y")
    # Graficar los resultados en líneas
    ax.plot([fecha] * len(inv["resultados"]), inv["resultados"], marker="o", label=inv["nombre"])

# Personalizar el gráfico
ax.set_title("Resultados de Investigaciones", fontsize=14)
ax.set_xlabel("Fecha", fontsize=12)
ax.set_ylabel("Resultados", fontsize=12)
ax.legend(title="Investigación", fontsize=10)

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
"""
while True:
     opcion=input ("digita opcion ")
     if opcion=="1":
          agregar(inventario)
