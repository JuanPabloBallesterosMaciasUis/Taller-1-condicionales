# Ejercicio No 6 :  Sumar los dos ultimos dijitos

print("--------------------------------------------------")
print("------SUMAR-LOS-DOS-ULTIMOS-NUMEROS-ES-UN-DIGITO------")
print("--------------------------------------------------")

#input
n = int(input("Digite un número de varios digitos:"))

#process
n1 = n % 10
n2 = int((n % 100) / 10)
s = n1 + n2

if s > 9:
    r = "es un número de 2 digitos."
else:
    r = "es un número de 1 digito."

#output
print("El número",n1,"y el",n2,"sumados",s,r)