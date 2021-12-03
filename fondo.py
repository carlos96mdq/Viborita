#La clase que maneja todo el tema del fondo
#Importamos los modulos necesarios


class Fondo:
	def __init__(self, color):
		self.color = color
		
	def dibujar(self, pantalla):
		pantalla.fill(self.color)