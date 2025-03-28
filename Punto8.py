# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal.
peso=float(input("Ingrese su peso en kilogramos:"))
altura=float(input("Ingrese su altura en metros:"))
indice_de_masa_corporal=peso/altura**2
print("El índice de masa corporal es:",indice_de_masa_corporal)
