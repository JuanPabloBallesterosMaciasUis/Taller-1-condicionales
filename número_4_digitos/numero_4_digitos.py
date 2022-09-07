# Ejercicio 3 : Numero de 4 digitos

print("------------------------------")
print("----Número de 4 digitos-------")
print("------------------------------")

#input
n =  int(input("Digite el número de 4 digitos : "))

#process
if n >= 1000 :
    if n <= 10000:
        r = "es de 4 dijitos "
    else:
        r = "es mayor de 4 digitos positvo"
else:
    r = "No es de 4 digitos"

#output
print("---------------------")
print("----RESULTADOS-------")
print("---------------------")

print( "El número",n ,r, )