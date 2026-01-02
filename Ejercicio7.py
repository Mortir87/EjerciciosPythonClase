#. Escribir una función que pida un número entero entre 1 y 10, lea el fichero tablan.txt con la tabla 
# de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero 
# no existe debe mostrar un mensaje por pantalla informando de ello. (2 punto)
#	***Ejemplo de ejecución:***
#	Introduce un número entero entre 1 y 10: 4 
#	4 x 1 = 4 
#	4 x 2 = 8 
#	4 x 3 = 12 
#	4 x 4 = 16 
#	4 x 5 = 20 
#	4 x 6 = 24 
#	4 x 7 = 28 
#	4 x 8 = 32 
#	4 x 9 = 36 
#	4 x 10 = 40

#El fichero para el "3" no existe.

continuar = True

while continuar:
    numero = int(input("Introduce un numero entero entre 1 y 10: "))
    if numero < 1 or numero > 10:
        continuar  = False
        print(f"El numero {numero} introducido esta fuera del rango indicado")
    else:
        # intentamos abrir el archivo en modo lectura con try 
        print(f"Tabla de multiplicar del numero: {numero}")
        try:
            with open(f"ejercicio7/tabla{numero}.txt", "r") as f:
                for linea in f:
                    print(linea.strip()) # evitamos saltos de linea

        except FileNotFoundError:
            print(f"El fichero tabla{numero}.txt no existe")
