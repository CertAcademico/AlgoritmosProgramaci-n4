import time

otr = "si"
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Bienvenido a PMD Focus>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Por favor ingrese su nombre: ")
Nombre= input()
print(f"Hola {Nombre} por favor ingrese su edad: ")
edad = input()
print (f"{Nombre} cual es el uso que quiere darle a PMD Focus , 1. Estudio, 2. Trabajo, 3. Lectura, 4. Otro: ")
uso = int(input())
if uso == 4:
    
    print("Por favor introduzca la opción del uso: ")
    uso = input ()
lista = [Nombre, edad, uso]
if uso == 1:
    lista[2] = "Estudio"""
elif uso == 2:
    lista[2] = "Trabajo"
elif uso == 3:
    lista[2] = "Lectura"
print (lista)
print("Esta es su lista ¿ desea cambiar algún dato ? 1. Si, 2. No: ")
des1 = str(input())
if des1 == "1":
    print("¿Que dato desea cambiar? 1. Nombre, 2. edad, 3. uso: ")
    des2 = str(input())
    if des2 == "1":
        print("Introduzca el nuevo nombre que desea tener en la app: ")
        lista[0] = str(input () )# se puede remplazar por un ciclo
        print("Esta es la lista actualizada")
        print (lista)    

    elif des2 == "2":
        print("Introduzca la nueva edad que desea tener en la app: ")
        lista[1] = str(input ())
        print("Esta es la lista actualizada")
        print (lista)    

    elif des2 == "3":
        print("Introduzca el nuevo uso que desea tener en la app: ")
        lista[2] = str(input ())
        print("Esta es la lista actualizada")
        print (lista)    

    else: 
        print("Por favor introduzca un valor valido")

print("Perfecto,continuemos")
while otr == "si":
    print("Por favor introduzca el tiempo que desea concentrarse (1. 20 minutos, 2. 30 minutos, 3. 45 minutos, 4. 60 minutos): ")
    tiempo = str(input())
    if tiempo == "1":
        print ("Usted ha elegido un tiempo de concentración de 20 minutos, esto significa que no tendrá descansos, de acuerdo a lo recomendado, esta bien o desea cambiarlo (si/no) : ")
        timc= str(input())
        if timc == "si":
            print("Por favor introduzca el tiempo que desea concentrarse (1. 30 minutos, 2. 45 minutos, 3. 60 minutos):")
            tiempo == str(input())
            if tiempo == "1":
                tiempo = "2"
    elif tiempo == "2":
        print("Usted tendra un periodo de concentración de 20 minutos, luego 5 minutos de descanso y luego otros 5 minutos de concentración, esta bien o desea cambiarlo (si/no) :")
        timc = str(input())
        if timc == "si":
            print("Por favor introduzca el tiempo que desea concentrarse (1. 20 minutos, 2. 45 minutos, 3. 60 minutos): ")
            tiempo == str(input())
            if tiempo == "2":
                tiempo = "3"
    elif tiempo == "3":
        print("Usted tendra un periodo de concentración de 25 minutos, luego 5 minutos de descanso y luego otros 15 minutos de concentración, esta bien o desea cambiarlo (si/no) :")
        timc = str(input())
        if timc == "si":
            print("Por favor introduzca el tiempo que desea concentrarse (1. 20 minutos, 2. 30 minutos, 3. 60 minutos): ")
            tiempo == str(input())
            if tiempo == "3":
                tiempo = "4"
    elif tiempo == "4":
        timc = str(input("Usted tendra un periodo de concentración de 30 minutos, luego 10 minutos de descanso y luego otros 20 minutos de concentración, esta bien o desea cambiarlo (si/no) :"))
        if timc == "si":
            tiempo == str(input("Por favor introduzca el tiempo que desea concentrarse (1. 20 minutos, 2. 30 minutos, 3. 45 minutos):  "))
    if tiempo == "1":
        print("Usted ha elegido un tiempo de concentración de 20 minutos, esto significa que no tendrá descansos de acuerdo a lo recomendado")
    elif tiempo == "2":
        print("Usted tendra un periodo de concentración de 20 minutos, luego 5 minutos de descanso y luego otros 5 minutos de concentración")
    elif tiempo == "3":
        print("Usted tendra un periodo de concentración de 25 minutos, luego 5 minutos de descanso y luego otros 15 minutos de concentración")
    elif tiempo == "4":
        print("Usted tendra un periodo de concentración de 30 minutos, luego 10 minutos de descanso y luego otros 20 minutos de concentración")
        
    BEG = str()
    while BEG != "LISTO":
        print("Cuando este listo para que el cronometro comineza intoduzca la palabra LISTO")
        BEG= str(input())
    if tiempo == "1":
        con = 1200
        for x in range (con, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El periodo de concentración ha terminado, esperamos hayas culminado tu tarea con exito")
        
        
    if tiempo == "2":
        con1 = 1200
        for x in range (con1, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El primer periodo de concentración ha terminado, ahora comenzarán sus 5 minutos de descanso")
        desc= 300
        for x in range (desc, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El tiempo de descanso ha terminado, ahora iniciara el segundo periodo de concentración")
        con2 = 300
        for x in range (con2, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
            
        
    if tiempo == "3":
        con1 = 1500
        for x in range (con1, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El primer periodo de concentración ha terminado, ahora comenzarán sus 5 minutos de descanso")
        desc= 300
        for x in range (desc, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El tiempo de descanso ha terminado, ahora iniciara el segundo periodo de concentración")
        con2 = 900
        for x in range (con2, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
    

    if tiempo == "4":
        con1 = 1800
        for x in range (con1, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El primer periodo de concentración ha terminado, ahora comenzarán sus 5 minutos de descanso")
        desc= 600
        for x in range (desc, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            time.sleep(1)
        print ("El tiempo de descanso ha terminado, ahora iniciara el segundo periodo de concentración")
        con2 = 1200
        for x in range (con2, 0, -1):
            seg = x % 60
            minut = int(x / 60)
            hr = int(x / 3600)
            print(f"{hr:02}: {minut:02} : {seg:02}")
            
    print ("El periodo de concentración ha terminado, esperamos hayas culminado tu tarea con exito")
    print ("¿Desea iniciar otro periodo de concentración? si/no")
    otr = str(input())
if otr == "no":
    print ("Gracias por acudir a este programa útil para sacar la mejor eficiencia a tu tiempo, nos vemos de nuevo en otra ocasión")