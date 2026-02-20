#
# Programación modular
# Hacer un programa que lea la matricula de un coche y la velocidad a la que circula y que calcule 
# u muestre en pantalla la multa a la que puede ser impuesto de pendiendo de
# si la velocidad a la que circula es menor de 120 km/h denominarlo sin multa o colocarle de 
# multa cero euros, si la velocidad supera los 120 y es menor a 140 Km/h la multa será de 100 euros 
# en cambio si supera los 140 km/h la multa será 200 euros.  el programa debe ser hecho para 3 coches y 
# calcular el monto total de multas.
# hacerlo de forma modular.

# se evaluará originalidad (no usar inteligencia artificial, se quiere desarrollar la lógica de programación)
# enviarlo en formato notepad o hacer  video ejecutando


# leer matricula (pedir 3 coches)
# mostrar en pantalla si tiene multa o no tiene multa dependiendo de la velocidad
# si la multa es de 120 a 140 son 100€ si es mas de 140km/h son 200€
# calcular la suma de las multas.

# funcion para definir el tipo de multa
def tipo_multa(velocidad):
    if velocidad > 140:
        multa = 200
    elif velocidad > 120:
        multa = 100
    else:
        multa = 0    
    return multa

# funcion imprimir la suma total
def mostrar_suma(total, cantidad_vehiculos): 
    print(f"La suma total de las multas de los {cantidad_vehiculos} vehiculos es: {total} euros")

# funcion para leer la cantidad de vehiculos que hemos elegido
def leer_vehiculos(cantidad_vehiculos):
    total_multas = 0 
    for i in range(cantidad_vehiculos):
        matricula = input(f"Escribe la matricula del vehiculo numero {i+1}: ")
        velocidad = int(input(f"Escribe la velocidad del vehiculo con matricula {matricula}: "))
        multa_actual = tipo_multa(velocidad)
        if multa_actual == 0:
            print(f"El vehiculo {matricula} sabe por donde va! No ha tenido multa")
        else:
            print(f"El vehiculo {matricula} va como una bala y tiene un regalo de {multa_actual} euros")
        total_multas += multa_actual
    return total_multas


cantidad_vehiculos = int(input("Cuantos vehiculos quieres leer: "))
total = leer_vehiculos(cantidad_vehiculos)
mostrar_suma(total, cantidad_vehiculos)