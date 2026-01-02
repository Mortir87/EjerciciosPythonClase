#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
#Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle 
# que no se puede procesar el dato. (1 punto)
#	***Ejemplo de ejecución:***
#	 Letra: o 
#    Es vocal

letra = input("Introduce una letra del alfabeto: ")
while len(letra) != 1 or not letra.isalpha(): #aseguramos que sea 1 char, ni numero ni simbolo
    print("No se puede procesar el dato introducido.")
    letra = input("Introduce una letra del alfabeto: ")    

if letra.lower() in "aeiou":
    print(f"La letra {letra} es vocal")
else:
    print(f"La letra {letra} es consonante")
