# Ejercicio 8 : Ecuacion de segundo grado
import math
print("-----------------------------")
print("----ECUACIÓN-SEGUNDO-GRADO----")
print("-----------------------------")
print("")

#input
a = float(input("Ingresa el valor de a"))
b = float(input("Ingresa el valor de b"))
c = float(input("Ingresa el valor de c"))

#proceso y output
discriminante = (b*b) - (4*a*c)
if discriminante < 0:
    print("No tiene raíces reales")
else:
    if discriminante == 0:
        x = -b / (2 * a)
        print("La solución es {}".format(x))
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("x1 = {} y x2 = {}".format(x1,x2))