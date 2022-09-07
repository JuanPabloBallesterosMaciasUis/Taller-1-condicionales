# Ejercicio No 1 : Llamada telefonica

print("------------------------------")
print("----COSTO DE LA LLAMADA-------")
print("------------------------------")

#input

t = int(input("Digite el tiempo para la llamda en minutos :"))
    
#process
if t<=3:
    cost_t= 300

else:
    min = t - 3
    cost_a = min *50
    cost_t = cost_a +300

print("---------------------")
print("----RESULTADOS-------")
print("---------------------")

print("El tiempo ",t," minutos que duro la llamda, cuesta $",cost_t,)
