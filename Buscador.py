import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

from Funciones import promedio_poder_de_pelea 
from Datos import dbz_dict
import json


def guardar_json(una_lista):
    # Pedir al usuario la raza y la habilidad que está buscando
    razas = []
    for personaje in una_lista.values():
        razas.extend(personaje['raza'])
    razas_unicas = list(set(razas))
    razas_unicas.sort()

    print("Razas disponibles:")
    for raza in razas_unicas:
        print(f"- [{raza}]")
    raza = input("Ingrese la raza que está buscando: ")

    habilidades = []
    for personaje in una_lista.values():
        habilidades.extend(personaje['habilidades'])
    habilidades_unicas = list(set(habilidades))
    habilidades_unicas.sort()

    print("Habilidades disponibles:")
    for habilidad in habilidades_unicas:
        print(f"- [{habilidad}]")

    habilidad = input("Ingrese la habilidad que está buscando: ")
    
    # Crear una lista para guardar los personajes que cumplen con los criterios
    personajes_cumplen = []
    
    # Buscar en la base de datos de personajes aquellos que cumplan con los dos criterios ingresados
    for personaje in una_lista.values():
        if personaje['raza'] == raza and habilidad in personaje['habilidades']:
            # Crear un diccionario para el personaje que cumple con los criterios, y guardar el nombre, poder de ataque y habilidades que no fueron parte de la búsqueda
            personaje_cumple = {
                'nombre': personaje['nombre'],
                'poder_de_pelea': promedio_poder_de_pelea(personaje['poder_de_pelea']),
                'habilidades_extras': [habilidad_extra for habilidad_extra in personaje['habilidades'] if habilidad_extra != habilidad]
            }
            
            # Agregar el diccionario a la lista de personajes que cumplen con los criterios
            personajes_cumplen.append(personaje_cumple)
    
    # Guardar la lista de diccionarios en un archivo JSON
    nombre_archivo = f"{raza.replace(' ', '_')}_{habilidad.replace(' ', '_')}.json"
    nombre_archivo = nombre_archivo.replace('&', '').replace(':', '').replace('/', '')
    with open(nombre_archivo, 'w') as archivo:
        json.dump(personajes_cumplen, archivo)
    
    print(f"Se guardó el archivo {nombre_archivo} con los personajes que cumplen con la búsqueda.")

guardar_json(dbz_dict)