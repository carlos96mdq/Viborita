#La clase que maneja todo el tema de la viborita
#Importamos los modulos necesarios
import pygame, sys, os
from pygame.locals import * #Lo usa la clase Stage

class Viborita(pygame.sprite.Sprite):
	def __init__(self, im_dir, son_dir, nombre_im, nombre_son, sw, sh):
		pygame.sprite.Sprite.__init__(self)
		#Cargo la imagen y creo el rectangulo de colision
		self.image = pygame.image.load(os.path.join(im_dir, nombre_im))
		self.sonido = pygame.mixer.Sound(os.path.join(son_dir, nombre_son))	
		self.rect = [self.image.get_rect()]
		self.rect[0].centerx = int(sw / 2)
		self.rect[0].centery = int(sh / 2)
		self.long = 3 #cantidad de bloques
		self.speed = 150  # 35 pixeles / 150 milisegundos
		self.dt = 0 #lo utilizo para regular cuantos milisegundos pasaron en cada update, mas que nadaporque el pixel es int y no float
		self.dire = 0 #0 derecha, 1 abajo, 2 izqueirda, 3 arriba
		self.updated = False #usada para regular apretar flechas muy rapido
		for x in range(1, self.long): #creo los demas bloques
			self.rect.append(self.image.get_rect())
			self.rect[x].centerx = self.rect[x-1].centerx - 35
			self.rect[x].centery = self.rect[x-1].centery

	def colision(self, manzana):
		if self.rect[0].colliderect(manzana.rect):
			self.long += 1
			#self.sonido.play() #es muy molesto el hdp
			self.rect.append(self.image.get_rect())
			self.rect[self.long-1].centerx = self.rect[self.long-2].centerx
			self.rect[self.long-1].centery = self.rect[self.long-2].centery
		for bloque in range(1, self.long):
			if self.rect[0].colliderect(self.rect[bloque]):
				print("Perdiste")
				sys.exit(0)

	def update(self, dt, sw, sh):
		self.dt += dt 
		#Espero self.speed mseg para mover la vibora
		if self.dt >= self.speed: 
			#Muevo el resto del cuerpo, debe hacerse en orden descendente
			for bloque in range(self.long-1, 0, -1):
				self.rect[bloque].centerx = self.rect[bloque-1].centerx
				self.rect[bloque].centery = self.rect[bloque-1].centery
			#Muevo cabeza
			if self.dire == 0:
				self.rect[0].centerx += 35
			elif self.dire == 1:
				self.rect[0].centery += 35
			elif self.dire == 2:
				self.rect[0].centerx -= 35
			elif self.dire == 3:
				self.rect[0].centery -= 35
			#Detecto si sali de la pantalla
			if self.rect[0].top <= -35 or self.rect[0].bottom >= sh+35 or self.rect[0].left <= -35 or self.rect[0].right >= sw+35:
				print("Perdiste")
				sys.exit(0)
			#Reinicio el conteo
			self.dt -= self.speed
			self.updated = True

	def dibujar(self, pantalla):
		for i in range(0, self.long):
			pantalla.blit(self.image, (self.rect[i].centerx, self.rect[i].centery))

