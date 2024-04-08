# Definición de las columnas del inventario
columnas = ["id", "nombre", "cantidad", "precio"]

# Inicialización del inventario con algunos productos predefinidos
inventario = {
    'Té Surtido Tetrapack 200ml x6und': {'id': 1, 'cantidad': 50, 'precio': 7450},
    'Cerveza Lata 330ml x6und': {'id': 2, 'cantidad': 50, 'precio': 9000},
    'Agua Pet 600ml x6und': {'id': 3, 'cantidad': 100, 'precio': 7200},
    'Gaseosa Naranja Pet 250ml x6und': {'id': 4, 'cantidad': 80, 'precio': 9000},
    'Agua Tónica Cero Vidrio 300ml x6und': {'id': 5, 'cantidad': 50, 'precio': 12000},
    'Energizante Lata 250ml x4und': {'id': 6, 'cantidad': 40, 'precio': 26600},
    'Avena bolsa 200ml x6und': {'id': 7, 'cantidad': 30, 'precio': 9250},
    'JUgo Lulo Tetrapack 1L x1und': {'id': 8, 'cantidad': 40, 'precio': 4000},
}

# Función para aumentar el ID de un producto
def aumentar_id():
    nuevo_id = len(inventario) + 1
    return nuevo_id

# Función para verificar si un producto existe en el inventario
def existe(nombre):
    if nombre not in inventario:
        print("El producto no existe en el inventario")
        return False
    return True

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad, precio):
    if nombre not in inventario:
        inventario[nombre] = {'id':aumentar_id(),'cantidad': cantidad, 'precio': precio}
        print(f"Producto '{nombre}' agregado al inventario.")
    else:
        print(f"El producto '{nombre}' ya existe en el inventario.")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para actualizar un producto en el inventario
def actualizar_producto(nombre_actual, nuevo_nombre=None, nuevo_precio=None):
    if nombre_actual in inventario:
        producto = inventario.pop(nombre_actual)
        if nuevo_nombre:
            producto['nombre'] = nuevo_nombre
        if nuevo_precio:
            producto['precio'] = int(nuevo_precio)
        inventario[nuevo_nombre] = producto
        print(f"Producto '{nombre_actual}' actualizado en el inventario.")
    else:
        print(f"El producto '{nombre_actual}' no existe en el inventario.")

# Función para mostrar todos los productos en el inventario
def mostrar_inventario():
    total_precio = 0
    print("Productos en el inventario:")
    for nombre, producto in inventario.items():
        print(f"{producto['id']}|{nombre}|{producto['cantidad']}|{producto['precio']}")
        total_precio += producto['cantidad'] * producto['precio']
    print(f"Total del precio de los productos en el inventario: {total_precio}")

# Bucle principal para interactuar con el inventario
while True:
    print("------------------Bienvenidos a MoShii-------------------")
    print("-------------------Digita una opcion--------------")
    print("           Mostrar Inventario digita:  1")
    print("           Agregar Producto digita:    2")
    print("           Eliminar Producto digita:   3")
    print("           Actualizar Producto digita: 4")
    print("           Salir de la APP digita:     X")

    opcion = input("Digita Una Opcion: ")
    if(opcion == "1"):
        mostrar_inventario()
    elif(opcion == "2"):
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        agregar_producto(nombre,precio,cantidad)
    elif(opcion == "3"):
        nombre = input("Nombre del producto: ")
        eliminar_producto(nombre)
    elif(opcion == "4"):
        nombre = input("Nombre del producto: ")
        if(existe(nombre)==False):continue
        nuevo_nombre = input("Nuevo nombre del producto: ")
        nuevo_precio = int(input("nuevo precio del producto: "))
        actualizar_producto(nombre,nuevo_nombre,nuevo_precio)
    elif(opcion == "X"):
        print("----------- Salistesss ------------")
        break
    else:
        print("---------Opcion no existe-----------")
