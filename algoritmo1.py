#Diseñar un algortimo que calcule la resta de
#2 numeros si el primero numero es impar.
#Caso contrario, que calcule la division

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if not num1%2==0:
    res = num1 - num2
    print("La resta de ", num1, " menos ", num2, " es igual a: ", res)
else:
    div = num1/num2
    print("La división de ", num1, " entre ", num2, " es igual a: ", div)

        
