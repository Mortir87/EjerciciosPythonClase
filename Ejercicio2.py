# Escribir un programa que, dado un número entero, muestre su valor absoluto. Recuerda que, 
# para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), 
# mientras que, para los negativos, su valor absoluto es el (el valor absoluto de -52 es 52). (1 punto) 
#	***Ejemplo de ejecución:***
#	Número: -12
#   Valor absoluto: 12

numero = int(input("Escribe un numero entero y te devuelvo el valor absoluto: "))
print(f"El valor absoluto de {numero} es {abs(numero)}")