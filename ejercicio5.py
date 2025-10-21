"""
Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F
"""

nota=int(input("ingrese su calificación: "))

if 90<= nota <=100:
    print("Su clasificación es: A")
elif 80<= nota <=89:
    print("Su clasificación es: B")
elif 70<= nota <=79:
    print("Su clasificación es: C")
elif 60<= nota <=69:
    print("Su clasificación es: D")
else:
    print("Su clasificación es: F")