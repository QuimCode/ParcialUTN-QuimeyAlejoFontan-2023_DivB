#---------------------------------------------------------------------------------------------------------#

import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

#---------------------------------------------------------------------------------------------------------#

from Funciones import *

def imprimir_datos_normalizados(una_lista):
    for id, personaje in una_lista.items():
        nombre = personaje['nombre']
        raza = ' -- '.join(personaje['raza'])
        poder_pelea = ' -- '.join(str(p) for p in personaje['poder_de_pelea'])
        poder_ataque = ' -- '.join(str(p) for p in personaje['poder_de_ataque'])
        habilidades = ' -- '.join(personaje['habilidades'])
        print(f"{id} | Nombre: {nombre} | Raza: {raza} | Poder de Pelea: {poder_pelea} | Poder de Ataque: {poder_ataque} | Habilidades: {habilidades}")
