"""Diseñar un algoritmo que clasifique las notas de grado según el
rango establecido"""

nota= float(input("Ingrese la nota de grado, a continuación: "))

def asignacion(num):
    if num<10.0 and num>9.0:
        letr = "A"
    elif num<9.0 and num>8.0:
        letr = "B"
    elif num<8.0 and num>7.0:
        letr = "C"
    elif num<7.0 and num>6.0:
        letr = "D"
    else:
        letr = "E"
    return letr


print("Su nota es:", asignacion(nota))
