from Datos import *
from Funciones import *
from Impreciones import imprimir_datos_normalizados
from Juego import *

print("Menú:")
print("1. Mostrar diccionario Normalizado")
print("2. Listar cantidad por raza")
print("3. Listar personajes por raza")
print("4. Listar personajes por habilidad")
print("5. Empezar combate")
print("6. Salir")
    
opcion = input("Elija una opción: ")
while opcion != "7":
    if opcion == "1":
        imprimir_datos_normalizados(dbz_dict)
    elif opcion == "2":
        contar_personajes_por_raza(dbz_dict)
    elif opcion == "3":
        result = listar_personajes_por_raza(dbz_dict)
        print(result)
    elif opcion == "4":
        buscar_personajes_por_habilidad(dbz_dict)
    elif opcion == "5":
        jugar_batalla(dbz_dict)
    elif opcion == "6":
        jugar_batalla(dbz_dict)
    else:
        print("Opción inválida")
        
    opcion = input("Elija una opción: ")    
