# 1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
# cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
# un personaje puede tener más de una raza y más de una habilidad.

# 2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
# corresponden a esa raza.

# 3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
# personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
# repetirse en los distintos listados.

# 4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
# deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.

# 5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
# batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
# guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
# el nombre del perdedor. Ese archivo anexará cada dato.t

# 6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
# guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
# Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
# Nombre del archivo:
# Saiyan_Genki_Dama.Json
# Datos :
# Goten - 3000 - Kamehameha + Tambor del trueno
# Goku - 5000000 - Kamehameha + Super Saiyan 2

# 7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción

# 8. Salir del programa.
#---------------------------------------------------------------------------------------------------------#

import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

#---------------------------------------------------------------------------------------------------------#

from Datos import *

#---------------------------------------------------------------------------------------------------------#
print(f"----------------------")

def contar_personajes_por_raza(una_lista):
    razas = {}
    for personaje in una_lista.values():
        if 'raza' in personaje:
            if isinstance(personaje['raza'], list):
                for raza in personaje['raza']:
                    raza_normalizada = normalizar_raza(raza)
                    if raza_normalizada not in razas:
                        razas[raza_normalizada] = 0
                    razas[raza_normalizada] += 1
            else:
                raza_normalizada = normalizar_raza(personaje['raza'])
                if raza_normalizada not in razas:
                    razas[raza_normalizada] = 0
                razas[raza_normalizada] += 1
    return razas

print(f"----------------------")
#---------------------------------------------------------------------------------------------------------#

def listar_personajes_por_raza(una_lista):
    personajes_por_raza = {}

    for personaje in una_lista.values():
        for raza in personaje['raza']:
            raza_normalizada = raza.lower()
            if raza_normalizada not in personajes_por_raza:
                personajes_por_raza[raza_normalizada] = []
            personajes_por_raza[raza_normalizada].append((personaje['nombre'], personaje['poder_de_ataque']))

    output = ""
    for raza, personajes in personajes_por_raza.items():
        output += f"\nTipo de raza: {raza.capitalize()}\n"
        for personaje in personajes:
            output += f"- {personaje[0]}: {personaje[1]}\n"

    return output

#---------------------------------------------------------------------------------------------------------#

def promedio_poder_de_pelea(poder_de_pelea):
    return sum(poder_de_pelea)/len(poder_de_pelea)

def buscar_personajes_por_habilidad(una_lista):
    habilidad = input("Ingrese la habilidad que desea buscar: ")
    personajes_encontrados = []
    for personaje in una_lista.values():
        if habilidad in personaje['habilidades']:
            personajes_encontrados.append(personaje)

    if len(personajes_encontrados) == 0:
        print("No se encontraron personajes con esa habilidad.")
    else:
        print(f"Personajes con la habilidad '{habilidad}':")
        for personaje in personajes_encontrados:
            print(f"- [{personaje['nombre']}] | Su raza es {personaje['raza']} | Promedio del poder de pelea: [ {promedio_poder_de_pelea(personaje['poder_de_pelea'])} ]\n")




















# import os

# os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\Parcial')

# #---------------------------------------------------------------------------------------------------------#
# import csv
# import json
# import re

# from unidecode import unidecode
# from collections import defaultdict

# dbz_dict = defaultdict(lambda: defaultdict(list))

# dbz_dict = {}
# nombres_agregados = []

# with open('DBZ.csv', 'r') as archivo:
#     csv_reader = csv.reader(archivo)
#     for linea in csv_reader:

#         Id = linea[0].strip()
#         Nombre = linea[1].strip()

#         Raza = [re.sub(r'[^a-zA-Z_\s]+', '', unidecode(raza.strip())).strip() for raza in linea[2].split('-')]
#         if Nombre == 'Android 19':
#             Raza = ['Androide']
#         elif Nombre == 'Kibito':
#             Raza = ['Shinjin']

#         Poder_de_pelea = [int(valor.strip()) for valor in linea[3].split(',')]
#         Poder_de_ataque = [int(valor.strip()) for valor in linea[4].split(',')]
#         Habilidades = [" ".join([re.sub(r'[^a-zA-Z]+', '', unidecode(valor.strip())) for valor in habilidades.split()]) for habilidades in linea[5].split('|')]
        
#         if Nombre not in nombres_agregados:
#             dbz_dict[Id] = {
#                 'nombre': Nombre,
#                 'raza': Raza,
#                 'poder_de_pelea': Poder_de_pelea,
#                 'poder_de_ataque': Poder_de_ataque,
#                 'habilidades': Habilidades
#             }
#             nombres_agregados.append(Nombre)

# with open('Datos_normalizados_DBZ.json', 'w') as impresion:
#     json.dump(dbz_dict, impresion, indent=4)