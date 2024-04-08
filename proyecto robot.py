
from gpiozero import DistanceSensor, Robot
from time import sleep

# Configurar el sensor de ultrasonido
sensor = DistanceSensor(echo=18, trigger=17)

# Configurar los motores del robot
robot = Robot(left=(4, 14), right=(17, 18))

# Función para controlar el comportamiento del robot
def ayudar_a_cruzar():
    while True:
        distancia = sensor.distance * 100  # Convertir la distancia a centímetros
        if distancia < 50:  # Si la distancia es menor a 50 cm, detener al robot
            robot.stop()
            print("Esperando a peatones...")
            sleep(5)  # Esperar 5 segundos para permitir que los peatones crucen
        else:  # Si no hay peatones cercanos, avanzar hacia la intersección
            robot.forward()
            print("Caminando hacia la intersección...")
            sleep(1)

try:
    ayudar_a_cruzar()  # Llamar a la función principal
finally:
    robot.stop()  # Detener el robot al finalizar el programa
