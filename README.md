# reto_1_dev_senior
# #<p>
*Descripcion del proyecto gestion experimentos*

El proyecto Gestión de Experimentos es una herramienta interactiva desarrollada en Python que permite gestionar, analizar y visualizar experimentos científicos. El usuario puede registrar experimentos, agregar resultados numéricos, eliminar experimentos y generar informes, todo mientras se realiza un análisis estadístico y visual de los resultados obtenidos a lo largo de las investigaciones. 
</p>
*Descripcion del codigo:*
</p>

- init: Inicializa los datos del experimento, como el nombre, tipo, fecha y una lista de resultados.
- agregar_resultado: Permite agregar un resultado numérico. Si el resultado es 'fin', termina el proceso de adición de resultados.
- mostrar_informacion: Muestra el nombre, tipo, fecha y los resultados del experimento.
- obtener_analisis: Realiza un análisis de los resultados (promedio, máximo y mínimo) usando la librería statistics.
<p>
**Funciones del programa:
</p>


- agregar_experimento(inventario):usuario agregar un nuevo experimento con su nombre, tipo, fecha y resultados.
- visualizarExperimentos(inventario): Muestra una lista de los experimentos almacenados en el inventario, mostrando detalles como el nombre, tipo, fecha y los resultados de cada uno.
- calcular_estadisticas(inventario): Calcula y muestra estadísticas básicas (promedio, máximo y mínimo) para los experimentos que tengan al menos 3 resultados registrados.
- generar_informe(inventario): Genera un archivo de texto (informe_investigaciones.txt) con un resumen de todos los experimentos almacenados, incluyendo nombre, tipo, fecha y resultados.
- eliminarExperimento(inventario): Permite al usuario eliminar un experimento del inventario, buscando por nombre. Si no encuentra el experimento, se le notifica al usuario.
- mostar_menu(): Muestra el menú principal de la aplicación con opciones para gestionar experimentos, realizar análisis de datos, generar informes y salir del programa.
- subMenu(): Muestra un submenú con opciones específicas para la gestión de experimentos, tales como agregar, mostrar o eliminar experimentos.
- main(): Es el ciclo principal del programa, que coordina la ejecución del menú principal y la interacción con el usuario. Aquí se gestionan las opciones del menú, la navegación a submenús y la ejecución de las funciones correspondientes.

<p>
##Menu principal:
</p>
Ofrece al usuario un menú interactivo con opciones para agregar experimentos, mostrar experimentos, eliminar experimentos, generar un informe o salir del programa.

*Menu:*
1. Agregar Experimento
2. Mostrar Experimentos
3. Eliminar Experimento
4. Generar Informe
5. Salir

*Menu:*
1. Agregar Experimento
2. Mostrar Experimentos
3. Eliminar Experimento
4. Generar Informe
5. Salir

*Menu:*
1. Agregar Experimento
2. Mostrar Experimentos
3. Eliminar Experimento
4. Generar Informe
5. Salir

<p>
*Carectiristicas del programa:*
</p>

- Entrada interactiva: Los datos del experimento se ingresan desde la consola.
- Análisis estadístico: El programa calcula el promedio, máximo y mínimo de los resultados del experimento.
- Generación de informe: El programa crea un archivo de texto con los detalles de todos los experimentos.
- Eliminación de experimentos: Puedes eliminar un experimento ingresando su nombre.

##Variables principales.
inventario: Es una lista que almacena los experimentos ingresados por el usuario. Cada experimento es un diccionario con claves como nombre, tipo, fecha y resultados.

*Ciclo while y estructuras de control*
El programa hace uso de varios ciclos while para mantener el flujo de interacción con el usuario hasta que este decida salir. Las opciones de los menús son gestionadas mediante if-else, permitiendo navegar entre las distintas funciones del programa.  


