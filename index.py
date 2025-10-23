#Respuestas Eduardo
# 1
num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2

print ("Suma:", suma)
print ("Resta:", resta)
print ("Multiplicación:", multiplicacion)
print ("División:", division)  
print ("Módulo:", modulo)

# 2
res = int(input("Ingrese un número para calcular: "))

cuadrado = res ** 2
cubo = res ** 3

print("El cubo del número es:", cubo)
print("El cuadrado del número es:", cuadrado)

#3
valor = int(input("Ingrese un número para calcular si es negativo, positivo o 0: "))

if valor > 0:
    print("El número es positivo")
elif valor < 0:
    print("El número es negativo")
else:
    print("El número es 0")

#4
divisible = int(input("Ingrese un número para verificar si es divisible por 3 y 5: "))

if divisible % 3 == 0 and divisible % 5 == 0:
    print("El número es divisible")
else:
    print("El número no es divisible")

#5
nota = int(input("Ingrese la nota del estudiante: "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
    
#6
numMayor = int(input("Ingrese el primer número: "))
numMenor = int(input("Ingrese el segundo número: "))
if numMayor > numMenor:
    print("El número mayor es:", numMayor)
elif numMenor > numMayor:
    print("El número mayor es:", numMenor)
else:
    print("Ambos números son iguales")

#7
parInpar = int(input("Ingrese un número para verificar si es par o impar: "))
if parInpar % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")