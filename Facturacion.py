#Sebastian Castellanos Carvajal y Christian Felipe Chacon Murillo

#Importamos el modulo os para identificar el sistema operativo en el cual el programa se va a ejecutar
import os

#Definimos terminal_limpia para poder ejecutar el codigo cls en caso de ser windows o clear para otros sistemas operativos
def terminal_limpia():
    os.system('cls' if os.name == 'nt' else 'clear')

#Definimos una lista en la cual vamos a guardar los productos que se van a agregar
Productos = []

#Definimos el precio de la propina en 0 para no tener errores en caso de no agregar propina
Precio_Propina = 0
#Definimos la propina en 0 para no tener errores en caso de no agregar propina
Propina=0

print("Este programa se encuentra en fase Beta, por lo cual es propenso a contener errores")
print("________________________________________________________________________________")
print("                         Programa Generador de Facturas                         ")
print("")

#Le preguntamos al usuario el numero de la factura y lo guardamos en la variable Num_Fact
Num_Fact = int(input("Numero de Factura: "))

#Le preguntamos al usuario la fecha de la factura y lo guardamos en la variable Fecha
Fecha = input("Fecha (Día/Mes/Año): ")

#Le preguntamos al usuario el nombre del cliente y lo guardamos en la variable Nombre_Cliente
Nombre_Cliente = input("Nombre Del Cliente: ")
print("")

#Ponemos un while adjuntar la cantidad de productos que el usuario necesite
while True:

    #Le preguntamos al usuario el nombre del producto
    Nombre_Producto = input("Ingresa el nombre del producto o (salir) para dejar de agregar productos: ")

    #Si el cliente escribe "salir" el ciclo while se rompe
    if Nombre_Producto == "salir":
        break

    #Le preguntamos al usuario el precio del producto ingresado
    try:
        Precio_Producto = float(input("Ingresa el precio del producto: "))

    #Si se digita un valor inesperado se mostrara un mensaje de error
    except ValueError:
        print("Por favor, ingresa un precio válido.")
        continue

    #Agregamos en la lista los productos con sus respectivos precios con .append
    Productos.append((Nombre_Producto, Precio_Producto))

#Separamos unicamente los precios que se encuentran en la lista, los sumamos y los agregamos en la variable Precio_Total
Precio_Total = sum(Precio for _, Precio in Productos)
print("")

#Utilizamos un while en caso de que el usuario digite otro numero
while True:
    
    #Le preguntamos al usuario si desea agregar propina
    try:
        Opcion1 = int(input("Desea agregar una propina - (1)Si - (2)No: "))

    #Si se digita un valor inesperado se mostrara un mensaje de error
    except ValueError:
        print("Por favor, ingresa un valor válido.")
        continue

    #Le preguntamos al usuario cual es la propina que se desea aplicar
    if Opcion1 == 1:

        while True:
            #Le preguntamos al usuario la propina que desea agregar, esto en porcentaje
            try:
                print("Recuerda, según la Ley 1935 de 2018 la ropina esta limitada sobre 10% del valor final del producto")
                print("")
                print("Ingrese el porcentaje de la propina que se desea aplicar")
                Propina = float(input("Ingrese unicamente el numero: "))

            #Si se digita un valor inesperado se mostrara un mensaje de error
            except ValueError:
                print("Por favor, ingresa un valor válido.")
                continue

            #Si la propina es menor al 10% se rompe el ciclo 
            if Propina <= 10:
                break

            #Si la propina supera el 10% se le vuelve a preguntar al usuario la propina a aplicar
            else:
                print ("El valor ingresado supera la suma permitida, vuelve a intentarlo")
                print ("")

        #Calculamos el valor de la propina y lo agregamos en la variable Precio_Propina      
        Precio_Propina = ((Precio_Total*Propina)/100)
        break

    #Le informamos al usuario que no se aplicara propina   
    elif Opcion1 == 2:
        print("No se agregara propina")
        break

    #Si el usuario digita otro numero se mostrara el mensaje de opcion invalida y se le volvera a preguntar si desea agregar propina
    
    else:
        print("Opción Invalida")

#Calculamos el precio final, sumando el precio de los productos y la propina
Precio_Final = Precio_Total + Precio_Propina

#Limpiamos la terminal para el usuario, pero aún seguimos conservando los datos 
terminal_limpia()

#Imprimimos los datos registrados
print("")
print("________________________________________________________________________________")
print("                                    Factura                                     ")
print("")
print("     Factura No.",Num_Fact)
print("")
print("     Fecha: ",Fecha)
print("     Nombre: ",Nombre_Cliente)
print("________________________________________________________________________________")
print("                               Lista de productos                               ")
print("")

#Utilizamos un for para imprimir todos los productos registrados
for Producto, Precio in Productos:
    print("    ",Producto,": COP",Precio)

print("")
print("     Precio de los productos: COP",Precio_Total)
print("")
print("     Propina del ",Propina,"% : COP",Precio_Propina)
print("________________________________________________________________________________")
print("")
print("     Precio Final: COP",Precio_Final)
print("")
