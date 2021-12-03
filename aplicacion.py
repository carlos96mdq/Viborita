#Donde se ejecutra toda la aplicacion
#Importamos los modulos necesarios
from fondo import *
from viborita import *
from manzana import *
from menu import *



#Constantes
IMG_DIR = "imagenes"
SON_DIR = "sonidos"
S_X = 250
S_Y = 75
S_WIDTH = 800
S_HEIGHT = 600
COLOR = (30, 145, 255)
FPS = 60

class Aplicacion:
	def __init__(self):
		#Se cargan los objetos
		self.fondo = Fondo(COLOR)	
		self.viborita = Viborita(IMG_DIR, SON_DIR, "viborita.jpg", "viborita.ogg", S_WIDTH, S_HEIGHT)
		self.manzana = Manzana(IMG_DIR, "manzana.jpg", S_WIDTH, S_HEIGHT)
		self.menu = Menu()
		self.dt = 0
		self.clock = pygame.time.Clock()

	def iniciar(self):
		#Creo pantalla
		self.pantalla = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
		pygame.display.set_caption("Viborita 2.0")
		self.viborita.image = self.viborita.image.convert()
		self.manzana.image = self.manzana.image.convert()
		self.menu.titulo = self.menu.titulo.convert()

	def colision(self):
		self.viborita.colision(self.manzana)
		self.manzana.colision(self.viborita, S_WIDTH, S_HEIGHT)

	def update(self):
		self.viborita.update(self.dt, S_WIDTH, S_HEIGHT)

	def teclado(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#La X de la ventana
				sys.exit(0)
			#Controlo movimiento de viborita y salida del juego
			elif event.type == pygame.KEYDOWN and self.viborita.updated == True:
				if event.key == K_RIGHT and self.viborita.dire != 2:
					self.viborita.dire = 0
					self.viborita.updated = False
				elif event.key == K_DOWN and self.viborita.dire != 3:
					self.viborita.dire = 1
					self.viborita.updated = False
				elif event.key == K_LEFT and self.viborita.dire != 0:
					self.viborita.dire = 2
					self.viborita.updated = False
				elif event.key == K_UP and self.viborita.dire != 1:
					self.viborita.dire = 3
					self.viborita.updated = False
				elif event.key == K_ESCAPE:
					sys.exit(0)
	
	def dibujar(self):
		self.fondo.dibujar(self.pantalla)
		self.manzana.dibujar(self.pantalla)
		self.viborita.dibujar(self.pantalla)		
		pygame.display.flip()
		
	



