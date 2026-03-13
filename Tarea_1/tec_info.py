"""DOCUMENTACIÓN
Universidad: Instituto Tecnológico de Costa Rica
Escuela: Ingeniería en Computadores
Curso: Introducción a la programación CE1101
Grupo 4
Versión: 3.14.2
Estudiantes: Diego Herrera Rivera, Joshua Sharbell Andrade Pérez
Descripción: Uso de 2 funciones diferentes de 4 librerías investigadas en el lenguaje de python, además, creación de una librería propia por medio de import.
Versión del programa: 1.0
Requerimientos del sistema: Intérprete python 3.7 o superior, Multiplataforma, no requiere dependencias, Procesador x86, x64 o ARM, Mínimo 256MB de RAM, 1MB de espacio libre"""

import sys
def get_about_info():
    return """Universidad: Instituto Tecnológico de Costa Rica
    Escuela de Ingeniería en Computadores
    Curso: Introducción a la Programación (CE1101)
    Año: 2026
    Grupo 4
    Versión de Python: """ + str(sys.version)