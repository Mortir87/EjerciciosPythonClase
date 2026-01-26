# Buenas estimados alumnos quiero que me programen en python lo siguiente:
# hacer un programa que lea una cadena de caracteres que contiene la información de la dirección de un correo electrónico ejemplo consorcio@odover.com y que tenga como salida:
# a.- solo el nombre del correo. para este ejemplo consorcio.
# b.- el nombre de la empresa. para este ejemplo odover
# c.- el dominio. para este ejemplo: com
# d.- Si no tiene @ enviar mensaje explicando que no cumple con los requisitos de ser un correo electrónico.
# Por favor traten de hacerlo por ustedes mismos es para que aprendan a tener lógica de programación.


texto = input("Escribe tu email: ")

#ejercicio D
if "@" not in texto:
    print("No cumple los requisitos de ser un correo electronico")
else:
    nombre = texto.split("@") #ahora es una lista
    empresa = nombre[1].split(".")

    #ejercicio A
    print(f"El nombre de usuario es: ", nombre[0])
    #ejercicio B
    print(f"El nombre de la empresa es: ", empresa[0])
    #ejercicio C
    print(f"El dominio es: ", empresa[-1]) # empresa[1] seria valido tambien, pero con -1 aseguramos la ultima posicion de la lista

    # Se podria realizar con un while, para que no cierre el progrema si no es correcto el correo electronico
