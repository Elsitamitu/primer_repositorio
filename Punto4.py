# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.
pi=3.14159
radio=float(input("Ingrese el radio del círculo :"))
perímetro=float(2*pi*radio)
área=float(pi*radio**2)
print("El área del circulo es:",área,"y su perímetro es:",perímetro)

