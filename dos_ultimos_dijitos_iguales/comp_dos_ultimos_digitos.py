#ejercicio No.5: Comparar si los dos ultimos dígitos de un número son iguales
 
print("-------------------------------------------------")
print("------COMPARACIÓN-DE-LOS-DOS-ULTIMOS NUMERO------")
print("-------------------------------------------------")

#input
n = int(input("Digite un número de varios digitos:"))

#process
n1 = n % 10
n2 = int((n % 100) / 10)

if n1 == n2:
    r = "es el mismo número."
else:
    r = "son números distintos."

#output
print("El número",n1,"y el",n2,r)