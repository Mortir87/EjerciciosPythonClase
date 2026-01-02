# Escribir un programa que, dado un número por el usuario, muestre todos sus divisores positivos.
# Recuerda que un divisor es aquel que divide al número de forma exacta (con resto 0). (1 punto)
#	***Ejemplo de ejecución:***
#	Número: 14 
#	Divisores: 1 2 7 14

numero = int(input("Escribe un numero y te dare sus divisores:"))
print(f"Los divisores de {numero} son: ")
for i in range(1, numero // 2 + 1): #evitamos el 0, division entera(//) hasta la mitad de numero
    if numero % i == 0: # utilizamos el resto
        print(i)
        
