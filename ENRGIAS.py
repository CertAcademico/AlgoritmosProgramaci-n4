import webbrowser

imagen = 'C:\Users\danie\OneDrive\Documentos\Nueva carpeta (3)\CONSUMO ELECTRODOMESTICOS.jpg'

webbrowser.open (imagen)

def calcular_consumo_anual(consumo_mensual):

    """
    Calcula el consumo anual de energía a partir del consumo mensual.
    
    consumo_mensual (float): Consumo mensual de energía en kWh.

    Consumo anual de energía en kWh.

    """
    return consumo_mensual * 12

def sugerir_tamaño_panel_solar(consumo_total):

    """
    Sugiere el tamaño del panel solar adecuado basado en el consumo total.
    
    consumo_total (float): Consumo total anual de energía en kWh.
    
     Sugerencia sobre el tamaño del panel solar adecuado.
    """
    if consumo_total <= 2000:
        return "Para su consumo es necesario de 2-4 placas solares (su consumo es bajo)."
    elif consumo_total <= 4000:
        return "Para su consumo es necesario de 4-6 placas solares (su consumo es medio-bajo)."
    elif consumo_total <= 6000:
        return "Para su consumo es necesario de 7-9 placas solares (su consumo es medio)."
    elif consumo_total <= 8000:
        return "Para su consumo es necesario de 10-15 placas solares (su consumo es medio-alto)."
    elif consumo_total <= 10000:
        return "Para su consumo es necesario de 16-20 placas solares (su consumo es alto)."
    else:
        return "Es posible que necesites considerar una instalación de energía solar más grande."
    
Nombre = (str(input("Bienvenido, te invitamos a escribir tu nombre :)")))

print("Bienvenido  " ,Nombre, "  estamos contentos que estes con nosotros; este es un programa beta muy practico para direccionarte en la cantidad de paneles solares necesarios para tu hogar")

print("----------------------------------------------------------------------------------------------------------------------------------------------------")

print("A continuación está el consumo de algunos electrodomésticos en Kwh: Nevera 55 kWh, Congelador 47 Kwh, Lavadora 22Kwh, Televisión 20 Kwh, Horno, 20 Kwh, secadora 18Kwh")


def main():
    consumo_total = 0
    while True:
        electrodomestico = input("Ingrese el nombre del electrodoméstico (o 'salir' para terminar): ")
        if electrodomestico.lower() == 'salir':
            break
        consumo_mensual = float(input(f"Ingrese el consumo mensual de {electrodomestico} en kWh: "))
        consumo_anual = calcular_consumo_anual(consumo_mensual)
        consumo_total += consumo_anual
        print(f"El consumo anual de {electrodomestico} es {consumo_anual} kWh.\n")
    
    print(f"El consumo total anual es {consumo_total} kWh.")
    print(sugerir_tamaño_panel_solar(consumo_total))

if __name__ == "__main__":
    main()