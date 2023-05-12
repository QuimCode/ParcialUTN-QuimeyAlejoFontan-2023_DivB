import os
os.chdir('C:\\Users\\quima\\OneDrive\\Escritorio\\Github\\Python\\ParcialUTN-QuimeyAlejoFontan-2023_DivB')

import csv
import re
from unidecode import unidecode

def normalizar(cadena):
    cadena_normalizada = re.sub(r'[^a-zA-Z0-9_\s]+', '', unidecode(cadena.strip())).strip()
    return cadena_normalizada

def normalizar_nombre(nombre):
    return normalizar(nombre)

def normalizar_raza(raza):
    raza_separada = raza.split('-')
    
    valores_normalizados = []
    for valor in raza_separada:
        valor_normalizado = re.sub(r'[^a-zA-Z_\s]+', '', unidecode(valor.strip())).strip()
        valores_normalizados.append(valor_normalizado)
    
    if len(valores_normalizados) == 1:
        return valores_normalizados[0]
    else:
        return valores_normalizados

def normalizar_poder_de_pelea(poder_de_pelea):
    poder_de_pelea_normalizado = [int(valor.strip()) for valor in poder_de_pelea.split(',')]
    return poder_de_pelea_normalizado

def normalizar_poder_de_ataque(poder_de_ataque):
    poder_de_ataque_normalizado = [int(valor.strip()) for valor in poder_de_ataque.split(',')]
    return poder_de_ataque_normalizado

def normalizar_habilidades(habilidades):
    habilidades_normalizadas = []
    habilidades_separadas = habilidades.split('|')
    for habilidad in habilidades_separadas:
        habilidad_normalizada = re.sub(r'[^a-zA-Z ]+', '', unidecode(habilidad.strip()))
        habilidad_normalizada = re.sub(r'\s+', ' ', habilidad_normalizada) 
        habilidades_normalizadas.append(habilidad_normalizada.strip())
    return habilidades_normalizadas



dbz_dict = {}
nombres_agregados = []

with open('DBZ.csv', 'r', encoding='utf-8') as archivo:
    csv_reader = csv.reader(archivo)
    for linea in csv_reader:

        Id = linea[0].strip()
        Nombre = normalizar_nombre(linea[1])

        Raza = normalizar_raza(linea[2])

        Poder_de_pelea = normalizar_poder_de_pelea(linea[3])

        Poder_de_ataque = normalizar_poder_de_ataque(linea[4])

        Habilidades = normalizar_habilidades(linea[5])

        if Nombre not in nombres_agregados:
            dbz_dict[Id] = {
                'nombre': Nombre,
                'raza': Raza,
                'poder_de_pelea': Poder_de_pelea,
                'poder_de_ataque': Poder_de_ataque,
                'habilidades': Habilidades
            }
            nombres_agregados.append(Nombre)
