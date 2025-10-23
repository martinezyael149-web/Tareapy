"""Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo)."""


num1= int(input("ingresa el primer número: "))
num2= int(input("ingrese el segundo número: "))

suma=num1+num2
resta=num1-num2
mult=num1*num2
div=num1/num2
div_ent=num1//num2
mod=num1%num2

print(f"La suma es: {suma}, la resta es: {resta}, la multiplicación es: {mult}, la division es: {div}, la division entera es: {div_ent}, el modulo es: {mod}")

      
      