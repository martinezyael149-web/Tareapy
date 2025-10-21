"""Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5."""

num=int(input("Ingrese un número: "))

if num%3==0 and num%5==0:
   print("El número ingresado es divisible por 3 y por 5")
else:
   print("El número ingresado no es divisible")