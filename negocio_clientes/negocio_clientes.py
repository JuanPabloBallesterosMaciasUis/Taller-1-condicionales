# Ejercicio No 9 :  CLientes G Y A

print("---------------------------------------")
print("----------DESCUENTO O RECARGO----------")
print("---------------------------------------")

#input
c = int(input("Elija 1 para cliente general o 2 para cliente afiliado: "))

#process
if c == 1:
    p = input("Para el metodo de pago elija 1 para al contado o 2 para plazos: ")
    if p == 1:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.15
        d2 = d + d1
    else:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.10
        d2 = d - d1
else:
    p = input("Para el metodo de pago elija 1 para al contado o 2 para plazos: ")
    if p == 2:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.5
        d2 = d + d1
    else:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.20
        d2 = d - d1

#output
print("---------------------")
print("------RESULTADOS-----")
print("---------------------")

print("El total a pagar es ",d2)

