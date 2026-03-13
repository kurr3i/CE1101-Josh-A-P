"""Las bibliotecas en los códigos ayudan a incorporar funciones y demás útiles sin tener que
programarlas desde cero, aquí hay cuatro bibliotecas que se pueden usar en python y sus
ejemplos con descripción, y para usarlas se debe escribir 'import' y su nombre."""

# MATH: usada para cálculos matemáticos más complejos que operaciones básicas,
# tambien guarda constantes importantes, como el número pi y trabaja con numeros reales.

import math

# Ej. 1) Función de raíz cuadrada
"""      Importado de math, se llama a la función sqrt() y se guarda el resultado en una
         variable, luego se imprime."""

raizcalc = math.sqrt(49)
print("Raiz de 49:", raizcalc)

# Ej. 2) Calculo de funciones trigonométricas usando pi
"""      Se llama a la función sin(), por ejemplo, y se usa la constante pi para calcular el
         seno de pi/2, se guarda en una variable y se imprime el resultado."""

sencalc = math.sin(math.pi/2)
print("Seno de pi/2 en radianes:", sencalc)

# RANDOM: genera valores aleatorios, que sirve para juegos y/o simulaciones.

import random

# Ej. 1) Numero entero aleatorio
"""      Genera un número aleatorio llamando a la función randint() y dándole un rango de
         valores, luego lo guarda en una variable y se imprime."""

randy = random.randint(1, 10)
print("Numero al azar:", randy)

# Ej. 2) Reacomodo aleatorio de lista
"""      Con una lista, se llama a la función shuffle() que mezcla aleatoriamente todos los
         elementos de la lista, y se imprime."""

lista = [1, 2, 3, "quesito", "stop"]
random.shuffle(lista)
print("Reorden:", lista)

# TIME: Mide tiempo y puede pausar programas.

import time

# Ej. 1) Pausa
"""      Con la función sleep(), se puede detener el código por un tiempo deseado (en s)."""

print("En espera, 5 segundos")
time.sleep(5)
print("En marcha")

# Ej. 2) Tiempo actual del sistema
"""      Devuelve con time() el tiempo transcurrido en segundos desde el 1/1/1970."""

print("Tiempo transcurrido desde inicio de 1970:", time.time())

# OS: Esta biblioteca permite interactuar con el sistema operativo de la compu, a través del
# manejo de carpetas, archivos y rutas de almacenamiento.

import os

# Ej. 1) Listar archivos de una carpeta
"""      Importado os, se pueden mostrar en la terminal los archivos del directorio actual
         con la función listdir()."""

print("Archivos en este directorio:", os.listdir())

# Ej. 2) Verificar existencia
"""      La función path.exists() verifica si un archivo de cierto nombre y formato existe,
         y lo devuelve como un valor booleano True o False."""

print("Existe el archivo:", os.path.exists("Hello_world.txt"))



#Creación de una librería propia //J$AP
import tec_info
r=tec_info.get_about_info()
print(r)