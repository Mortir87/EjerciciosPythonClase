# Escribir un programa que permita al usuario ingresar números enteros. La repetición terminará cuando 
# el usuario ingrese un número para el cual la suma de sus dígitos sea mayor que 1000 ó múltiplo de 5.
#  Finalmente, mostrar cuántos números impares ingresó el usuario antes de cortar la repetición. (2 punto)
#	***Ejemplo de ejecución:***
#	 Escribí un número: 16 
#	 Escribí un número: 922 
#	 Escribí un número: 1513 
#	 Escribí un número: 481 
#	 Escribí un número: 90 
#	 Cantidad de impares: 2
contador = 0
continuar = True

while continuar:
    numero = int(input("Escribe un numero: "))
    if numero % 2 != 0:
        contador += 1

    suma = sum(int(d) for d in str(abs(numero))) #convertimos a string para poder recorrer la lista
    # con abs evitamos error si introducen valores negativos

    if suma > 1000 or numero % 5 == 0:
        continuar = False
print(f"Cantidad de numeros impares: {contador}")