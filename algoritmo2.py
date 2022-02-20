#Diseñar un algoritmo que presente el resultado de las operaciones matemáticas.


for num1 in range(1,4):
    num2=1
    while num2<=3:
        mult= num1*num2
        print(num1," * ",num2," = ",mult)
        num2 = num2 + 1
    num1 += 1
