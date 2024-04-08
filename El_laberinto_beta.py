#proyecto el laberinto
import random
def Pantalla_inicio():
    print ("Elige uan opcion")
    print ("1. jugar")
    print ("2. salir")
    eleccion = input()
    if eleccion == '1':
        print("Bienvenido al laberinto")
        juego()
    elif eleccion == '2':
        salida()
    else:
        print ("instruccion no valida")
        Pantalla_inicio()
    return

def salida():
    salir = input ("¿Deseas salir? " )
    if salir == 'si':
        print ("Hasta luego")
    elif salir == 'no':
        Pantalla_inicio()
    elif salir == '':
         salida()
    return

def juego():
    opcion1 = input("Puedes girar a la derecha o a la izquierda, ¿que decides? " )
    if opcion1 == 'izquierda':
        opcion2 = input("ves tres direcciones, izquierda derecha y frente, elige una " )
        if opcion2 == 'frente':
            print ("Ves algo que brilla al fondo del pasillo")
            print ("Encuentras un dado misterioso y una nota")
            print ("                    9d                  ")
            print ("¿Deseas usar el dado?")
            print ("si")
            print ("no")
            uso = input()
            if uso == 'si':
                dado_misterioso = [1,2]
                uso1 = random.choice(dado_misterioso)
                if uso1 == 1:
                    print ("El dado te libera del laberinto")
                    print ("Felicidades")
                elif uso1 == 2:
                    print ("El dado te ha condenado")
                    print ("Has perdido")
            elif uso == 'no':
                print ("podras volver a usar el dado en opciones especiales mas adelante")
                print ("debes regresar y tomar entre izquierda y derecha")
                opcion3 = input ()
                if opcion3 == 'derecha':
                    print ("Escuchas pasos extraños acercadose, ves una puerta con el numero 5e ¿deseas entrar?")
                    print ("si")
                    print ("no")
                    puerta = input()
                    if puerta == 'si':
                        print ("encuentras un arma y el ente que escuchas se acerca violentamente ¿que decides hacer?")
                        print ("1.usar dado misterioso")
                        print ("2.usar el arma")
                        decision = input()
                        if decision == '1':
                            print ("Decides usar el dado")
                            dado_misterioso = [1,2]
                            uso1 = random.choice(dado_misterioso)
                            if uso1 == 1:
                                print ("El dado te libera del laberinto")
                                print ("Felicidades")
                            elif uso1 == 2:
                                print ("El dado te ha condenado")
                                print ("Has perdido")
                        if decision == '2':
                            print ("Decides usar el arma")
                            print ("acabas con el ente y suelta un mapa del laberinto que contiene el numero 4c")
                            print ("Lograste encontrar la salida")
                    elif puerta == 'no':
                        print ("El ente se acerca y acaba contigo")
                        print ("Has muerto")
                elif opcion3 == 'izquierda':
                    print ("Sientes que la salida esta cerca ")
                    print ("Ves una luz pero para pasar debes responder la siguiente pregunta")
                    print ("¿Cuanto es la raiz de dos medios multiplicado por 274?")
                    respuesta = int(input())
                    if respuesta == 274:
                        print (respuesta, " Es correcto")
                        print ("La luz es una puerta de salida")
                        print ("Has logrado salir del laberinto")
                    else:
                        print (respuesta, " Es incorrecto")
                        print ("Tienes 2 intentos mas")
                        respuesta = int(input())
                        if respuesta == 274:
                            print (respuesta, " Es correcto")
                            print ("La luz es una puerta de salida")
                            print ("Has logrado salir del laberinto")
                        else:
                            print (respuesta, " Es incorrecto")
                            print ("Tienes 1 intento mas")
                            respuesta = int(input())
                            if respuesta == 274:
                                print (respuesta, " Es correcto")
                                print ("La luz es una puerta de salida")
                                print ("Has logrado salir del laberinto")
                            else:
                                print (respuesta, " Es incorrecto")
                                print ("Ves al fondo el numero 2f")
                                print ("La luz desaparece dejandote atrapado en el laberinto por siempre")
                                print ("Has perdido")
        if opcion2 == 'derecha':
                    print ("Escuchas pasos extraños acercadose, ves una puerta ¿deseas entrar?")
                    print ("si")
                    print ("no")
                    puerta = input()
                    if puerta == 'si':
                        print ("encuentras un arma y el ente que escuchas se acerca violentamente")
                        print ("Decides usar el arma")
                        print ("acabas con el ente y suelta un mapa del laberinto que contiene el numero 4c")
                        print ("Lograste encontrar la salida")
                    elif puerta == 'no':
                        print ("El ente se acerca y acaba contigo")
                        print ("Has muerto")                                
        elif opcion2 == 'izquierda':
                    print ("Sientes que la salida esta cerca ")
                    print ("Ves una luz pero para pasar debes responder la siguiente pregunta")
                    print ("¿Cuanto es la raiz de dos medios multiplicado por 274?")
                    respuesta = int(input())
                    if respuesta == 274:
                        print (respuesta, " Es correcto")
                        print ("La luz es una puerta de salida")
                        print ("Has logrado salir del laberinto")
                    else:
                        print (respuesta, " Es incorrecto")
                        print ("Tienes 2 intentos mas")
                        respuesta = int(input())
                        if respuesta == 274:
                            print (respuesta, " Es correcto")
                            print ("La luz es una puerta de salida")
                            print ("Has logrado salir del laberinto")
                        else:
                            print (respuesta, " Es incorrecto")
                            print ("Tienes 1 intento mas")
                            respuesta = int(input())
                            if respuesta == 274:
                                print (respuesta, " Es correcto")
                                print ("La luz es una puerta de salida")
                                print ("Has logrado salir del laberinto")
                            else:
                                print (respuesta, " Es incorrecto")
                                print ("Ves al fondo el numero 2f")
                                print ("La luz desaparece dejandote atrapado en el laberinto por siempre")
                                print ("Has perdido")                                        
    elif opcion1 == 'derecha':
        print ("Ves un cartel")
        print ("¿Las opciones no son extrañas, no lo crees?")
        print ("Te encuentras con la opcion de ir a la derecha o a la izquierda, ¿Que decides?")
        opcion2b = input()
        if opcion2b == 'derecha':
            print ("ves una nota en el suelo")
            print ("Te sientes muy afortunado 😀")
            print ("              3a              ")
            print ("Ves un camino al frente y otro a la derecha")
            opcion3b = input()
            if opcion2b == 'derecha':
                print ("solo ves un muro al final")
                print ("Ves algo escrito en el muro")
                print ("buen intento pero solo terminaste en una perdida de tiempo")
                print ("Ahora comenzaras denuevo")
                juego()
        elif opcion2b == 'izquierda':
            print ("El pasillo te lleva directamente hacia la derecha")
            print ("solo encuentras una nota")
            print ("No hay salida")
            print ("      6b       ")
            print ("Solo podras tomar el camino de la derecha")
            print ("ves una nota en el suelo")
            print ("Te sientes muy afortunado 😀")
            print ("              3a              ")
            print ("Ves un camino al frente y otro a la derecha")
            opcion3b = input()
            if opcion3b == 'derecha':
                print ("solo ves un muro al final")
                print ("Ves algo escrito en el muro")
                print ("buen intento pero solo terminaste en una perdida de tiempo")
                print ("Ahora comenzaras denuevo")
                juego()
            elif opcion3b == 'frente':
                print ("Ves una puerta con codigo y un letrero que dice:")
                print ("Si has buscado bien en anteriores oportunidades sabras como salir")
                print ("Solo puedes usar numeros, no letras")
                codigo = int(input())
                if codigo == 364952:
                    print ("La puerta se abre con exito")
                    print ("Has encontrado la verdadera salida")
                    print ("Eres libre")
                else:
                    print ("Codigo incorrecto")
    return
    
print ("-----------------------------------------------------------------------")
print ("El laberinto (juego de opciones)")
print ("-----------------------------------------------------------------------")
print ("                                               version sujeta a errores")
Pantalla_inicio()