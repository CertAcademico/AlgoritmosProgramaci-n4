# Programa interactivo para aprender a programar en Python

# Bienvenida al usuario
print("¡Bienvenido al programa interactivo para aprender a programar en Python!")

# Explicación inicial
print("Este programa te guiará a través de varios conceptos básicos de programación en Python.")

# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, introduce tu nombre: ")

# Saludar al usuario
print(f"Hola, {nombre}!")

# Explicación de variables y tipos de datos
print("En programación, utilizamos variables para almacenar información.")
print("Hay diferentes tipos de datos en Python, como enteros, flotantes, cadenas de caracteres, booleanos y diccionarios.")

# Ejemplos de variables y tipos de datos
numero_entero = 10
numero_flotante = 3.14
cadena_caracteres = "Hola, mundo!"
es_verdadero = True
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Mostrar ejemplos de variables y tipos de datos
print("Aquí tienes algunos ejemplos de variables y sus valores:")
print("- Número entero:", numero_entero)
print("- Número flotante:", numero_flotante)
print("- Cadena de caracteres:", cadena_caracteres)
print("- Valor booleano:", es_verdadero)
print("- Diccionario:", mi_diccionario)

# Explicación de controles de flujo (if-elif-else)
print("Los controles de flujo nos permiten tomar decisiones en nuestro programa.")
print("Por ejemplo, podemos usar 'if' para ejecutar un bloque de código si se cumple una condición.")

# Ejemplo de control de flujo
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Explicación de bucles (for, while)
print("Los bucles nos permiten repetir bloques de código varias veces.")
print("Podemos usar 'for' para iterar sobre una lista de elementos y 'while' para repetir hasta que se cumpla una condición.")

# Ejemplo de bucle while
contador = 0
print("Contando hasta un número ingresado por el usuario:")
limite = int(input("Ingresa un número límite para contar: "))
while contador <= limite:
    print(contador)
    contador += 1

# Explicación de listas y sus métodos
print("Las listas son colecciones ordenadas de elementos.")
print("Podemos agregar elementos, quitar elementos, y acceder a ellos por su índice.")

# Ejemplo de manipulación de lista
numeros = [1, 2, 3, 4, 5]
numeros.append(6)  # Agregar un elemento al final de la lista
numeros.remove(3)  # Quitar un elemento de la lista
print("Lista de números después de manipularla:", numeros)

# Explicación de tuplas
print("Las tuplas son colecciones ordenadas e inmutables de elementos.")
print("A diferencia de las listas, las tuplas no se pueden modificar una vez creadas.")

# Ejemplo de tupla
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# Explicación de conjuntos
print("Los conjuntos son colecciones desordenadas y únicas de elementos.")
print("No permiten elementos duplicados y no tienen un orden definido.")

# Ejemplo de conjunto
colores = {"rojo", "verde", "azul", "rojo"}  # El elemento duplicado "rojo" se eliminará automáticamente
print("Colores:", colores)

# Explicación de diccionarios
print("Los diccionarios son colecciones desordenadas de pares clave-valor.")
print("Permiten almacenar información estructurada y acceder a ella por clave.")

# Ejemplo de diccionario
persona = {
    "nombre": input("Ingresa tu nombre: "),
    "edad": int(input("Ingresa tu edad: ")),
    "profesion": input("Ingresa tu profesión: "),
    "ciudad": input("Ingresa tu ciudad: ")
}
print("Información de la persona:", persona)

# Explicación de operadores
print("Los operadores se utilizan para realizar operaciones en Python.")
print("Existen operadores aritméticos, de comparación, lógicos, de asignación, y más.")

# Ejemplo de operadores
a = int(input("Ingresa un número entero: "))
b = int(input("Ingresa otro número entero: "))
print("Suma:", a + b)
print("Comparación:", a > b)
print("Operador lógico:", a > 5 and b < 10)

# Explicación de manejo de archivos
print("Python permite leer y escribir archivos en el sistema de archivos.")
print("Podemos abrir un archivo, escribir en él, leer su contenido, y cerrarlo cuando hayamos terminado.")

# Ejemplo de manejo de archivos
archivo = open("ejemplo.txt", "w")  # Abrir un archivo en modo escritura
archivo.write("¡Hola, mundo!\nEste es un ejemplo de archivo en Python.")
archivo.close()  # Cerrar el archivo

# Explicación de funciones
print("Las funciones nos permiten reutilizar código al encapsularlo en bloques de código que pueden ser llamados varias veces.")
print("Podemos definir nuestras propias funciones y también usar funciones integradas en Python.")

# Ejemplo de función
def suma(a, b):
    return a + b

num1 = int(input("Ingresa un número entero para sumar: "))
num2 = int(input("Ingresa otro número entero para sumar: "))
resultado_suma = suma(num1, num2)
print("Resultado de la suma:", resultado_suma)

# Explicación de módulos y librerías
print("Los módulos y librerías son conjuntos de funciones y clases que nos permiten extender las capacidades de Python.")
print("Podemos importar módulos y librerías externas para usar sus funciones y clases en nuestro programa.")

# Ejemplo de importación de módulo y uso de función
import math

numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))
raiz_cuadrada = math.sqrt(numero)
print("Raíz cuadrada:", raiz_cuadrada)

# Finalización del programa
print("¡Eso es todo por ahora!")
print("Espero que hayas aprendido mucho sobre programación en Python.")
