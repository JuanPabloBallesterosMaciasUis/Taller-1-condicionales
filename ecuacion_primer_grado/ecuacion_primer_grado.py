#ejercicio 7 .Ecuacion de primer grado

print("----------------------------------")
print("------Ecuacion de primer grado----")
print("----------------------------------")

#input
a =int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

print("La ecuación es: {}x + {} = 0 ".format(a,b))

# process y output
if a != 0:
    x = -b/a
    print("La respuesta es: x = {}".format(x))
else:
    if b == 0:
        print("La ecuación no tiene solución")
    else:
        print("La ecuación no tiene solución")