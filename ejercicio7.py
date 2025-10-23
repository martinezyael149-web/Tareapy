"""
Escribe un programa que solicite al usuario un número entero y
determine si es par o impar.
"""

num= int(input("Ingrese un número:"))

if num%2==0:
    print(f"El número ingresado {num} es par")
else:
    print(f"El número ingresado {num} es impar")