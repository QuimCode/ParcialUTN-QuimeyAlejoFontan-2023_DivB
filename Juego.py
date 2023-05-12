#---------------------------------------------------------------------------------------------------------#

import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

#---------------------------------------------------------------------------------------------------------#

import random
from Funciones import promedio_poder_de_pelea
from datetime import datetime

def jugar_batalla(personajes):
    personaje_usuario = input("Seleccione un personaje: ")
    personaje_maquina = random.choice(list(personajes.keys()))
    
    poder_usuario = promedio_poder_de_pelea(personajes[personaje_usuario]['poder_de_pelea'])
    poder_maquina = promedio_poder_de_pelea(personajes[personaje_maquina]['poder_de_pelea'])
    
    resultado = ""
    if poder_usuario > poder_maquina:
        resultado = f"Gana el usuario con el personaje ... {personaje_usuario}"
        ganador = personaje_usuario
        perdedor = personaje_maquina
    elif poder_maquina > poder_usuario:
        resultado = f"Gana la IA con el personaje ... {personaje_maquina}"
        ganador = personaje_maquina
        perdedor = personaje_usuario
    else:
        resultado = "Empate"
        ganador = None
        perdedor = None
    
    fecha = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open("registro_batallas.txt", "a") as archivo:
        if ganador and perdedor:
            registro = f"{fecha} - Ganador: {ganador}, Perdedor: {perdedor}\n"
        else:
            registro = f"{fecha} - {resultado}\n"
        archivo.write(registro)
        
    print(resultado)



    #     nombre_usuario = input("Seleccione un personaje: ")
    # personaje_usuario = None
    # for personaje in personajes.keys():
    #     if personaje['nombre'] == nombre_usuario:
    #         personaje_usuario = personaje
    #         break
    
    # if personaje_usuario is None:
    #     print("Personaje no encontrado")
    #     return
    
    # personaje_maquina = personajes[random.choice(list(personajes.keys()))]