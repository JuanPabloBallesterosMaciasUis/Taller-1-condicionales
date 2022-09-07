# Ejercicio No 4 :  Ultima cifra par

print("------------------------------")
print("----Ultima cifra par----------")
print("------------------------------")

#input
n = int(input("Digite un número: "))


#process
m = n % 2

if m==0:
    p = "es par"
else:
    p = "no es par"


#output
print("---------------------")
print("----RESULTADOS-------")
print("---------------------")

print("El ultimo digito de",n, p)