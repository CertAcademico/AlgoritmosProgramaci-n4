# Proyecto de ventas
nombres = []  # Lista para almacenar nombres de artículos
precios = []  # Lista para almacenar precios de artículos
cantidades_vendidas = []  # Lista para almacenar cantidades vendidas de artículos

def agregar_articulo():
    # Solicitar al usuario el nombre y el precio del artículo
    nombre = input("Ingrese el nombre del artículo: ")
    precio = float(input("Ingrese el precio del artículo: "))
    # Agregar el nombre y el precio a las listas correspondientes
    nombres.append(nombre)
    precios.append(precio)
    # Inicialmente, no se ha vendido nada del artículo, así que agregamos 0 a cantidades_vendidas
    cantidades_vendidas.append(0)
def hacer_venta():
    # Solicitar al usuario el nombre del artículo a vender
    nombre = input("Ingrese el nombre del artículo a vender: ")
    
    if nombre in nombres:  # Verificar si el artículo existe en la lista de nombres
        # Obtener el índice del artículo en la lista de nombres
        indice = nombres.index(nombre)
        
        # Solicitar al usuario la cantidad a vender
        cantidad = int(input("Ingrese la cantidad a vender: "))
        
        # Actualizar la cantidad vendida del artículo correspondiente
        cantidades_vendidas[indice] += cantidad
    else:
        # Informar al usuario que el artículo no existe en la lista
        print("El artículo no existe en la lista")
def mostrar_informacion():
    # Mostrar información de los artículos
    print("\nInformación de los artículos:")
    for i in range(len(nombres)):
        # Mostrar el nombre, el precio y la cantidad vendida de cada artículo
        print(f"Artículo: {nombres[i]}, Precio: ${precios[i]}, Cantidad vendida: {cantidades_vendidas[i]}")
    # Calcular el total de unidades vendidas
    total_vendido = sum(cantidades_vendidas)
    print(f"Total vendido: {total_vendido}")
# Menú principal
while True:
    print("\nMenú:")
    print("1. Introducir un artículo nuevo")
    print("2. Hacer una venta")
    print("3. Mostrar información")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))  # Solicitar al usuario que seleccione una opción

    if opcion == 1:
        agregar_articulo()  # Llamar a la función agregar_articulo si la opción es 1
    elif opcion == 2:
        hacer_venta()  # Llamar a la función hacer_venta si la opción es 2
    elif opcion == 3:
        mostrar_informacion()  # Llamar a la función mostrar_informacion si la opción es 3
    elif opcion == 4:
        break  # Salir del bucle si la opción es 4
    else:
        # Informar al usuario si la opción seleccionada es inválida
        print("Opción inválida. Intente nuevamente.")
