class Inventario:
 def __init__(self):
   self.vinos = {}

def agregar_vino(self, vino):
 self.vinos[vino.nombre.lower()] = vino

def obtener_vino(self, nombre_vino):
 return self.vinos.get(nombre_vino.lower())

def eliminar_vino(self, nombre_vino):
 del self.vinos[nombre_vino.lower()]

def actualizar_inventario(self, nombre_vino, cantidad):
  vino = self.obtener_vino(nombre_vino)
  if vino:
    vino.cantidad = cantidad
  else:
    print("El vino no está en el inventario.")
           