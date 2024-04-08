#Librerías
import tensorflow as tf #Biblioteca que permite por medio de "tf" acceder a todas las funciones de Tensorflow
import cv2 #Permite indentificar imagenes
import numpy as np #Permite realizar calculos matemáticos para tareas especificas

imagen_real=cv2.VideoCapture(0) #Permite iniciar la camara del dispositivo que se esta usando en este caso se pone (0), ya que solo hay una cámara a utilizar
while True:
        rectangulo,linea=imagen_real.read() #Permite leer o identificar la variable anterior que es la cámara que se va a utilizar
        cv2.imshow('Objeto', linea) #La función imshow permite mostrar la imagen captada e identificada por el read
        if cv2.waitKey(0): #Esta función se puede usar para que despues de un tiempo especifico se cierre la ventana en la que se esta captando la imagen(milisegundos)
            break #El ciclo se rompe cuando la función waitkey se cumple
        cv2.imwrite('Objeto.jpg', linea) #La función imwrite permite guardas imagenes en la ubicación dada
        cv2.destroyAllWindows()#Después de que el bucle se cumple la ventana se cerrará

#Permite crear el identificador con unas medidas especificas
obj=cv2.imread('Objeto.jpg', 0)
recort=obj[60:300, 230:380]#Allí se estan seleccionando las filas de la imagen desde la fila numero 61 hasta y la fila numero 299
cv2.imshow('Objeto', recort) #Se muestra en pantalla el objeto a identficar con el recorte realizado anteriormente

#Se repite el ciclo anterior para crear más variables y el programa pueda reconocer objetos
imagen_real=cv2.VideoCapture(0)
while True:
    
        rectangulo2,linea2=imagen_real.read()
        cv2.imshow('Identificar', linea2)
        if cv2.waitKey(0):
            break
        cv2.imwrite('Identificar.jpg', linea2)
        cv2.destroyAllWindows()
    
obj2=cv2.imread('Identificar.jpg', 3)
color= cv2.cvtColor(obj2,cv2. COLOR_BGR2GRAY)#Esta función permite pasar las imagenes que estan siendo reconocidas a una escala de grises lo cual indica que la imagen esta siendo procesada
cv2.imshow('Identificar', obj2)

a,b= recort.shape[::-1]#Tupla que representa el ancho (a) y el alto (b) para que el objeto tenga una figura que indique que fue el seleccionado
identificar=cv2.matchTemplate(color, recort, cv2.TM_CCOEFF_NORMED)#La funcion TM_CCOEFF_NORMED permite comparar las caracteristicas que posee la imagen y objetos
tamaño= 0.75 #Permite identificar con ayuda de la funcion matchTemplate la cual encuentra posisicones similares en las imagenes, es decir los objetos que son superiores a esta cifra van a ser los que estaran encasillados

ubicación=np.where(identificar >= tamaño) #Esta función permite encontrar las coincidencias entre objetos con ayuda de las variables (a) y (b), es decir con las filas y columnas
for pt in zip (*ubicación[::-1]): #Permite establecer las figuras que van a ser las que indican los objetos que contienen similitudes
      cv2.rectangle(obj2,pt,(pt[0]+a,pt[1]+b),(0, 0, 255),1) #Dibuja un rectangulo en todos los objetos que son similares con ayuda del ancho (a), (b). Allí ((0, 0, 255) indica el color del rectangulo y (1) es el grosor del rectangulo
      cv2.imshow('Identificar', obj2) #Permite mostrar la imagen que contiene la variable.