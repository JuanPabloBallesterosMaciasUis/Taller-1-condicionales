# Ejercicio con if No.2: Numero mayor de tres numeros.

print("---------------------------")
print("------MAYOR-3-ENTEROS------")
print("---------------------------")
print("")

#input

a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")
c = input("Ingrese el tercer número: ")

#proceso
#
if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c

#output
print("---------------------------")
print("---------RESULTADOS--------")
print("")

print("El número mayor entre", a,",",b,"y", c,"es: ", mayor