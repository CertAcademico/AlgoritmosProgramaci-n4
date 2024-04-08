import tkinter as tk
from tkinter import ttk, simpledialog
from PIL import Image, ImageTk
import threading
import time

# Base de datos de calorías por alimento
comida_calorias = {
    'Sandia': 47, 'Fresas': 49, 'Melon': 60, 'Durazno': 61, 'Moras': 62, 'Frambuesas': 65,
    'Ciruela': 76, 'Piña': 82, 'Arándanos': 85, 'Mango': 99, 'Kiwi': 110, 'Limón por 3 gramos': 19,
    'Tomate': 17, 'Uvas': 66, 'Mandarina': 46,
    'Garbanzos': 1090, 'Lentejas': 690, 'Frijoles': 346,
    'Espárragos': 15, 'Pimentón': 55, 'Brenjenas': 28, 'Apio': 9, 'Patatas': 234,
    'Aguacate': 136, 'Plátano': 84,
    'Calamar': 118, 'Anchoas': 185, 'Sardinas': 145, 'Atún': 274, 'Salmón': 210,
    'Huevo clara': 46, 'Huevo yema': 339, 'Pollo': 116, 'Lomo': 145, 'Chuleta de cerdo': 288,
    'Pavo': 108, 'Tofu': 82, 'Carne': 180,
    'Raviolis carne': 536, 'Canelones pollo': 780, 'Chocolate': 655, 'Helado': 259,
    'Pizza': 300, 'Pan': 130,
    'Leche achocolatada': 62, 'Leche en polvo': 36, 'Leche entera': 57, 'Leche descremada': 45,
    'Yogur con cereales': 48, 'Yogur con frutas y fibra': 71, 'Queso de cabra': 173, 'Queso crema': 245,
    'Queso cremoso': 245, 'Queso cheddar': 374, 'Queso ricotta': 185, 'Queso mozzarrella': 334,
    'Queso cottage': 95, 'Queso holandés': 398,
    'Arroz blanco': 123, 'Maiz': 98, 'Harina de trigo': 337, 'Pan trigo': 216,
    'Churros': 354, 'Dona': 456, 'Torta chocolate': 469
}

# Diccionario para almacenar las calorías consumidas
cal_consumidas = {}

# Contador de vasos de agua consumidos
vasos_agua = 0

# Diccionario para almacenar las rutinas y su estado
rutinas = {}

def ingresar_calorias():
    ventana_ingreso_calorias = tk.Toplevel(root)
    ventana_ingreso_calorias.title("Ingresar Calorías")

    def guardar_calorias():
        nombre = entry_nombre.get()
        alimento = alimento_seleccionado.get()
        calorias = comida_calorias.get(alimento, "Alimento no encontrado")

        if isinstance(calorias, int):
            if nombre:
                if nombre in cal_consumidas:
                    cal_consumidas[nombre] += calorias
                else:
                    cal_consumidas[nombre] = calorias
                print(f"Las calorías de {nombre} por el alimento '{alimento}' han sido registradas de forma exitosa.")
            else:
                print("Error: Debes ingresar tu nombre.")
        else:
            print(calorias)

    entry_nombre = ttk.Entry(ventana_ingreso_calorias, font=("Arial", 10))
    entry_nombre.grid(row=0, column=0, padx=10, pady=5)

    alimentos = list(comida_calorias.keys())
    alimento_seleccionado = tk.StringVar(ventana_ingreso_calorias)
    alimento_seleccionado.set(alimentos[0])
    menu_alimento = ttk.Combobox(ventana_ingreso_calorias, textvariable=alimento_seleccionado, values=alimentos, state="readonly")
    menu_alimento.grid(row=1, column=0, padx=10, pady=5)

    boton_guardar = tk.Button(ventana_ingreso_calorias, text="Guardar", command=guardar_calorias, font=("Arial", 10))
    boton_guardar.grid(row=2, column=0, pady=10)

def agregar_vasos_agua():
    global vasos_agua
    litros = simpledialog.askfloat("Agregar Agua", "Ingrese la cantidad de litros de agua que ha bebido:")
    if litros is not None:
        vasos_agua += litros * 1000
        print(f"Se han agregado {litros} litros de agua.")

def mostrar_calorias_consumidas():
    print("Calorías consumidas por persona:")
    for nombre, calorias in cal_consumidas.items():
        print(f"{nombre}: {calorias} calorías")

def mostrar_vasos_agua():
    global vasos_agua
    print(f"Vasos de agua consumidos en el día de hoy: {vasos_agua} ml")

def agregar_rutina():
    ejercicios_disponibles = ["Cardio", "Correr", "Saltar la cuerda", "Pesas", "Yoga", "Natación", "Ciclismo", "Flexiones", "Abdominales", "Sentadillas", "Zumba", "Pilates", "Kickboxing", "Escalada", "Crossfit"]

    ventana_agregar_rutina = tk.Toplevel(root)
    ventana_agregar_rutina.title("Agregar Rutina")

    ejercicios_seleccionados = []

    def seleccionar_ejercicio():
        ejercicio = ejercicio_var.get()
        if len(ejercicios_seleccionados) < 5 and ejercicio not in ejercicios_seleccionados:
            ejercicios_seleccionados.append(ejercicio)
            print(f"Ejercicio '{ejercicio}' seleccionado.")
        else:
            print("Error: Debe seleccionar un máximo de 5 ejercicios y no repetirlos.")

    def guardar_rutina():
        nombre_rutina = entry_nombre_rutina.get()

        if len(ejercicios_seleccionados) == 5 and nombre_rutina:
            print(f"Rutina guardada: {nombre_rutina}")
            rutinas[nombre_rutina] = {"ejercicios": ejercicios_seleccionados, "estado": "Pendiente"}
            print("Ejercicios seleccionados:")
            for ejercicio in ejercicios_seleccionados:
                print(ejercicio)
        else:
            print("Error: Debe seleccionar exactamente 5 ejercicios y especificar un nombre para la rutina.")

    tk.Label(ventana_agregar_rutina, text="Nombre de la Rutina:", font=("Arial", 10)).pack(pady=5)
    entry_nombre_rutina = ttk.Entry(ventana_agregar_rutina, font=("Arial", 10))
    entry_nombre_rutina.pack(pady=5)

    tk.Label(ventana_agregar_rutina, text="Seleccione 5 ejercicios:", font=("Arial", 10)).pack(pady=5)
    ejercicio_var = tk.StringVar(ventana_agregar_rutina)
    ejercicio_var.set(ejercicios_disponibles[0])
    menu_ejercicio = ttk.Combobox(ventana_agregar_rutina, textvariable=ejercicio_var, values=ejercicios_disponibles, font=("Arial", 10), state="readonly")
    menu_ejercicio.pack(pady=5)

    boton_agregar_ejercicio = tk.Button(ventana_agregar_rutina, text="Agregar Ejercicio", command=seleccionar_ejercicio, font=("Arial", 10))
    boton_agregar_ejercicio.pack(pady=5)

    boton_guardar_rutina = tk.Button(ventana_agregar_rutina, text="Guardar Rutina", command=guardar_rutina, font=("Arial", 10))
    boton_guardar_rutina.pack(pady=10)

def ver_estado_rutina():
    ventana_estado_rutinas = tk.Toplevel(root)
    ventana_estado_rutinas.title("Estado de Rutinas")

    for nombre, rutina in rutinas.items():
        tk.Label(ventana_estado_rutinas, text=f"Rutina: {nombre}, Estado: {rutina['estado']}", font=("Arial", 10)).pack(pady=5)

def cambiar_estado_rutina():
    ventana_cambiar_estado = tk.Toplevel(root)
    ventana_cambiar_estado.title("Cambiar Estado de Rutina")

    rutina_seleccionada = tk.StringVar(ventana_cambiar_estado)
    rutina_seleccionada.set(list(rutinas.keys())[0] if rutinas else "No hay rutinas")

    def cambiar_estado():
        estado = estado_var.get()
        rutina = rutina_seleccionada.get()
        if rutina:
            if rutina in rutinas:
                rutinas[rutina]["estado"] = estado
                print(f"Se cambió el estado de la rutina '{rutina}' a '{estado}'.")
            else:
                print(f"Error: La rutina '{rutina}' no existe.")
        else:
            print("Error: No hay rutinas disponibles.")

    tk.Label(ventana_cambiar_estado, text="Seleccione la rutina:", font=("Arial", 10)).pack(pady=5)
    menu_rutina = ttk.Combobox(ventana_cambiar_estado, textvariable=rutina_seleccionada, values=list(rutinas.keys()), font=("Arial", 10), state="readonly")
    menu_rutina.pack(pady=5)

    tk.Label(ventana_cambiar_estado, text="Seleccione el nuevo estado:", font=("Arial", 10)).pack(pady=5)
    estado_var = tk.StringVar(ventana_cambiar_estado)
    estado_var.set("Pendiente")
    menu_estado = ttk.Combobox(ventana_cambiar_estado, textvariable=estado_var, values=["Pendiente", "Realizada"], font=("Arial", 10), state="readonly")
    menu_estado.pack(pady=5)

    boton_cambiar_estado = tk.Button(ventana_cambiar_estado, text="Cambiar Estado", command=cambiar_estado, font=("Arial", 10))
    boton_cambiar_estado.pack(pady=10)

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))

def cargar_imagen_y_boton(boton, imagen_path, command, texto_boton):
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((40, 40))
    imagen = ImageTk.PhotoImage(imagen)
    boton.config(image=imagen, compound=tk.TOP, command=command, font=("Arial", 10), text=texto_boton)
    boton.image = imagen

root = tk.Tk()
root.title("GYMTrack")

ttk.Label(root, text="GYMTrack", font=("Arial", 20)).grid(row=0, columnspan=2, pady=10)

boton_ingresar_calorias = tk.Button(root)
boton_ingresar_calorias.grid(row=1, column=0, padx=10, pady=5)
cargar_imagen_y_boton(boton_ingresar_calorias, "calorias.jpeg", ingresar_calorias, "Ingresar Calorías")

boton_agregar_agua = tk.Button(root)
boton_agregar_agua.grid(row=1, column=1, padx=10, pady=5)
cargar_imagen_y_boton(boton_agregar_agua, "agua.jpeg", agregar_vasos_agua, "Agregar Agua")

boton_mostrar_calorias = tk.Button(root)
boton_mostrar_calorias.grid(row=2, column=0, padx=10, pady=5)
cargar_imagen_y_boton(boton_mostrar_calorias, "calorias1.jpeg", mostrar_calorias_consumidas, "Mostrar Calorías")

boton_mostrar_agua = tk.Button(root)
boton_mostrar_agua.grid(row=2, column=1, padx=10, pady=5)
cargar_imagen_y_boton(boton_mostrar_agua, "agua1.jpeg", mostrar_vasos_agua, "Mostrar Agua")

boton_agregar_rutina = tk.Button(root)
boton_agregar_rutina.grid(row=3, column=0, padx=10, pady=5)
cargar_imagen_y_boton(boton_agregar_rutina, "rutina.jpeg", agregar_rutina, "Agregar Rutina")

boton_ver_estado_rutina = tk.Button(root)
boton_ver_estado_rutina.grid(row=3, column=1, padx=10, pady=5)
cargar_imagen_y_boton(boton_ver_estado_rutina, "rutina3.jpeg", ver_estado_rutina, "Ver Estado Rutinas")

boton_cambiar_estado_rutina = tk.Button(root)
boton_cambiar_estado_rutina.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
cargar_imagen_y_boton(boton_cambiar_estado_rutina, "rutina1.jpeg", cambiar_estado_rutina, "Cambiar Estado Rutina")

centrar_ventana(root)
root.mainloop()
