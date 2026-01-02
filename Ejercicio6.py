# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, 
# (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes,
# (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente: (2 punto)
#	1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos. 
#	2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. 
#	3. Preguntar por el NIF del cliente y mostrar sus datos. 
#	4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre. 
#	5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre. 
#6. Terminar el programa
#
#	***Ejemplo de ejecución:*** 
#		Menú de opciones 
#		(1) Añadir cliente 
#		(2) Eliminar cliente 
#		(3) Mostrar cliente 
#		(4) Listar clientes 
#		(5) Listar clientes preferentes 
#		(6) Terminar 
#		Elige una opción: 1 
#		Introduce NIF del cliente: 11111111A 
#		Introduce el nombre del cliente: Pepito Pérez 
#		Introduce la dirección del cliente: Madrid 
#		Introduce el teléfono del cliente: 666555444 
#		Introduce el correo electrónico del cliente: pepito@gmail.com 
#		¿Es un cliente preferente (S/N)? S
#       ...

continuar = True
clientes = {}

while continuar:
    print("\nMenú de opciones")
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar clientes")
    print("(5) Listar clientes preferentes")
    print("(6) Terminar")
    
    opcion = input("Escoge una opcion de la lista: ")

    if opcion == "1":
        
        # Añadir cliente
        
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la direccion del cliente: ")
        telefono = input("Introduce el telefono del cliente: ")
        correo = input("Introduce el email del cliente: ")
        preferente = input("¿Es un cliente preferente (S/N)? ").strip().upper()
    
        clientes[nif] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }
        print(f"Cliente {nombre} añadido correctamente.")

    elif opcion == "2":
        
        # Eliminar cliente
        
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif] # podriamos utilizar clientes.pop(nif) si quisieramos mostrar lo eliminado
            print("Cliente eliminado correctamente.")
        else:
            print("El NIF no existe en la base de datos.")
    
    elif opcion == "3":
            
         # Mostrar cliente

        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            cliente = clientes[nif]
            print(f"\nDatos del cliente {cliente['nombre']}:")
            print(f"Direccion: {cliente['direccion']}")
            print(f"Telefono: {cliente['telefono']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Preferente: {cliente['preferente']}")
        else:
            print("El NIF no existe en la base de datos.")
        
    elif opcion == "4":
            
            # Listar todos los clientes

            if clientes:
                print("\nLista de todos los clientes:")
                for nif, cliente in clientes.items():
                    print(f"NIF: {nif}, Nombre: {cliente['nombre']}")
            else:
                print("No hay clientes en la base de datos.")

    elif opcion == "5":

        # listar preferentes

        preferentes = {nif: c for nif, c in clientes.items() if c["preferente"] == "S"}
        if preferentes: # si es true
            print("\nClientes preferentes:")
            for nif, cliente in preferentes.items():
                print(f"NIF: {nif}, Nombre: {cliente['nombre']}")
        else:
            print("No hay clientes preferentes en la base de datos.")

    elif opcion == "6":
         
         # terminar programa

         print("Programa terminado")
         continuar = False
    else:
        print("Opcion incorrecta, selecciona una opcion entre 1 y 6")