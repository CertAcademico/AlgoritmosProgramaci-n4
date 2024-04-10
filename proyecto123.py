import random
#Esta línea importa el módulo random, que se utilizará más adelante en el código para generar precios aleatorios para los vinos.

#- Aquí comienza la definición de la clase Vino, que se utilizará para representar los diferentes clases de vino.
class Vino:
    def __init__(self, nombre, tipo, region, descripcion, cosecha, grado_alcoholico, temperatura_consumo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.region = region
        self.descripcion = descripcion
        self.cosecha = cosecha
        self.grado_alcoholico = grado_alcoholico
        self.temperatura_consumo = temperatura_consumo
        self.precio = precio

# A continuacion se va a crear una clase de inventario en donde se cree un diccionario de los vinos 
class Inventario:
    def __init__(self):
        self.vinos = {}

    def agregar_vino(self, vino):
        self.vinos[vino.nombre.lower()] = vino

    def obtener_vino(self, nombre_vino):
        return self.vinos.get(nombre_vino.lower())

    def eliminar_vino(self, nombre_vino):
        del self.vinos[nombre_vino.lower()]


def obtener_informacion_vino(nombre_vino, inventario):
    vino = inventario.obtener_vino(nombre_vino)
    return vino


def mostrar_informacion_vino(vino):
    if vino:
        print(f"Información sobre {vino.nombre}:")
        print(f"Tipo: {vino.tipo}")
        print(f"Región: {vino.region}")
        print(f"Descripción: {vino.descripcion}")
        print(f"Cosecha: {vino.cosecha}")
        print(f"Grado alcohólico: {vino.grado_alcoholico}")
        print(f"Temperatura de consumo: {vino.temperatura_consumo}")
        print(f"Precio: ${vino.precio} pesos")
    else:
        print("Lo siento, este vino no lo tenemos en nuestro inventario")


def consejos_cata():
    print("Consejos para catar vinos:")
    print("- Observa el color y la transparencia del vino.")
    print("- Huele el vino para detectar sus aromas.")
    print("- Prueba el vino, prestando atención a su sabor, textura y final.")


def etiqueta_consumo():
    print("Sugerencias para etiqueta de consumo:")
    print("- Sirve el vino a la temperatura adecuada para su tipo.")
    print("- Acompaña el vino con alimentos que realcen su sabor.")


def generar_precios_aleatorios(inventario):
    for vino in inventario.vinos.values():
        vino.precio = round(random.uniform(10, 100), 3)


def main():
    inventario = Inventario()
    
    inventario.agregar_vino(Vino("Malbec", "Tinto", "Mendoza, Argentina",
                                  "Vino tinto de cuerpo medio con notas a frutos rojos y especias.",
                                  "2019", "13%", "16-18°C", round))
    inventario.agregar_vino(Vino("Chardonnay", "Blanco", "Borgoña, Francia",
                                  "Vino blanco seco con notas de frutas tropicales y mantequilla.",
                                  "2020", "12.5%", "8-10°C", round))
    inventario.agregar_vino(Vino("Merlot", "Tinto", "Bordeaux, Francia",
                                  "Vino tinto suave con notas de ciruelas y chocolate.",
                                  "2018", "14%", "16-18°C", round))
    inventario.agregar_vino(Vino("Sauvignon Blanc", "Blanco", "Marlborough, Nueva Zelanda",
                                  "Vino blanco refrescante con notas herbales y cítricas.",
                                  "2020", "12%", "6-8°C", round))
    inventario.agregar_vino(Vino("Pinot Noir", "Tinto", "Borgoña, Francia",
                                  "Vino tinto ligero con aromas a frutos rojos y especias.",
                                  "2019", "13%", "14-16°C", round))
    inventario.agregar_vino(Vino("Cabernet Sauvignon", "Tinto", "Napa Valley, Estados Unidos",
                                  "Vino tinto robusto con aromas a cassis y vainilla.",
                                  "2017", "14.5%", "16-18°C", round))
    inventario.agregar_vino(Vino("Riesling", "Blanco", "Mosela, Alemania",
                                  "Vino blanco semidulce con notas a frutas de hueso y miel.",
                                  "2018", "11%", "8-10°C", round))
    inventario.agregar_vino(Vino("Barolo", "Tinto", "Piamonte, Italia",
                                  "Vino tinto potente y complejo con aromas a cereza, regaliz y especias.",
                                  "2015", "14.5%", "18-20°C", round))
    inventario.agregar_vino(Vino("Brunello di Montalcino", "Tinto", "Toscana, Italia",
                                  "Vino tinto elegante con aromas a frutos rojos maduros y cuero.",
                                  "2016", "14%", "16-18°C", round))
    inventario.agregar_vino(Vino("Gato Negro", "Tinto", "Valle Central, Chile", "Vino tinto suave y afrutado con notas a bayas rojas y especias.",
                          "2019", "13.5%", "16-18°C",round))
    inventario.agregar_vino(Vino("Sancerre", "Blanco", "Loira, Francia", "Vino blanco fresco y mineral con aromas a lima y hierbas.",
                         "2020", "13%", "8-10°C",round))
    inventario.agregar_vino(Vino("Lambrusco", "Tinto", "Emilia-Romaña, Italia",
                                  "Vino espumoso italiano conocido por su sabor afrutado y ligero.",
                                  "NV", "11%", "8-10°C", round))
    inventario.agregar_vino(Vino("Cariñoso", "Tinto", "Valle Central, Chile",
                                  "Un vino chileno suave y afrutado, perfecto para compartir momentos especiales.",
                                  "2019", "13%", "16-18°C", round))
    inventario.agregar_vino(Vino("Prosecco", "Espumoso", "Véneto, Italia",
                                  "Espumoso italiano seco y refrescante con burbujas finas y persistentes.",
                                  "NV", "11%", "6-8°C", round))
    inventario.agregar_vino(Vino("Shiraz", "Tinto", "Barossa Valley, Australia",
                                  "Vino tinto australiano robusto y especiado con notas a moras y pimienta negra.",
                                  "2019", "14.5%", "16-18°C", round))
    inventario.agregar_vino(Vino("Champagne", "Espumoso", "Champagne, Francia",
                                  "El clásico vino espumoso francés, perfecto para celebraciones.",
                                  "NV", "12%", "6-8°C", round))
    inventario.agregar_vino(Vino("Zinfandel", "Tinto", "California, Estados Unidos",
                                  "Vino tinto californiano rico y afrutado con notas a zarzamoras y especias.",
                                  "2018", "15%", "16-18°C", round))
    inventario.agregar_vino(Vino("Viognier", "Blanco", "Ródano, Francia",
                                  "Vino blanco aromático con notas a melocotón, albaricoque y flores blancas.",
                                  "2020", "13.5%", "8-10°C", round))
    inventario.agregar_vino(Vino("Rioja", "Tinto", "La Rioja, España",
                                  "Vino tinto español con cuerpo y aromas a frutas maduras y vainilla.",
                                  "2017", "13.5%", "16-18°C", round))
    inventario.agregar_vino(Vino("Albariño", "Blanco", "Galicia, España",
                                  "Vino blanco gallego fresco y aromático con notas cítricas y florales.",
                                  "2020", "12.5%", "8-10°C", round))
    inventario.agregar_vino(Vino("Malvasía", "Blanco", "Canarias, España",
                                  "Vino blanco canario con cuerpo y aromas a frutas tropicales y miel.",
                                  "2019", "13%", "8-10°C", round))
    inventario.agregar_vino(Vino("Tempranillo", "Tinto", "Castilla-La Mancha, España",
                                  "Vino tinto español joven y frutal con notas a frutas rojas y especias.",
                                  "2020", "14%", "14-16°C", round))
    inventario.agregar_vino(Vino("Verdejo", "Blanco", "Rueda, España",
                                  "Vino blanco seco y aromático con notas a hierbas y frutas blancas.",
                                  "2019", "13%", "8-10°C", round))
    

    generar_precios_aleatorios(inventario)

    nombre_vino = input("Ingresa el nombre de tu vino favorito: ")
    vino = obtener_informacion_vino(nombre_vino, inventario)

    mostrar_informacion_vino(vino)

    opcion = input("¿Deseas recibir consejos para catar vinos? (si/no): ")
    if opcion.lower() == "si":
        consejos_cata()

    opcion = input("¿Deseas recibir sugerencias para la etiqueta de consumo? (si/no): ")
    if opcion.lower() == "si":
        etiqueta_consumo()

    opcion = print("Espero hayas aprendido sobre los diferentes tipos de vinos, buena suerte")


if __name__ == "__main__":
    main()

