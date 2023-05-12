#---------------------------------------------------------------------------------------------------------#

import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

#---------------------------------------------------------------------------------------------------------#

from Funciones import *

def imprimir_datos_normalizados(una_lista):
    for id, personaje in una_lista.items():
        nombre = personaje['nombre']
        raza = str(personaje['raza'])
        poder_pelea = ' -- '.join(str(p) for p in personaje['poder_de_pelea'])
        poder_ataque = ' -- '.join(str(p) for p in personaje['poder_de_ataque'])
        habilidades = ' -- '.join(personaje['habilidades'])
        print(f"{id} | Nombre: {nombre} | Raza: {raza} | Poder de Pelea: {poder_pelea} | Poder de Ataque: {poder_ataque} | Habilidades: {habilidades}")

def imprimir_cantidad_por_raza(una_lista):
    razas = contar_personajes_por_raza(una_lista)
    print(f"\nContador de razas:")
    for raza, cantidad in razas.items():
        print(f"-La raza de [{raza}] contiene a [{cantidad}] personajes/e\n")
