#Ejercicio 10. Orden de menor a mayor

print("-----------------------------")
print("----ORDENAR-DE-MENOR A MAYOR----")
print("-----------------------------")
print("")

#input
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

#proceso
if a <= b and a <= c:
    if b <= c:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(a,b,c))
    else:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(a,c,b))

elif b <= a and b <= c:
    if a <= c:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(b,a,c))
    else:
        print("El orden de los números de menor a mayor")

elif c <= a and c <= b:
    if a <= b:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(c,a,b))
    else:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(c,b,a))