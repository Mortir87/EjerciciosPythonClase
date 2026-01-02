# Escribir un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
# A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, 
# solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el 
# texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) 
# y almacenar este número en una variable llamada índice. Mostrar en pantalla el carácter del texto 
# ubicado en la posición dada por índice. (1 punto)

#	 ***Ejemplo de ejecución:***
#		Ingrese un texto: Hola qué tal
#		El carácter en primer lugar es: H 
#		Ingrese un número positivo menor a 12 
#			7
#		El carácter en esa posición es: é


texto = input("Ingrese un texto: ")
print("El carácter en primer lugar es:", texto[0])

# NOTA: input devuelve un string. Necesitamos un entero, tanto para la posicion del indice como para la validacion del while.
# Conversion INT necesaria.

indice = int(input(f"Ingrese un numero positivo entre 0 y {len(texto) - 1}: "))
while indice < 0 or indice >= len(texto):
    print("Numero para el indice no valido")
    indice = int(input(f"Ingrese un numero positivo entre 0 y {len(texto) - 1}: "))

print("El caracter en  la posicion indicada es: ", texto[indice])
