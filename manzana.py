#La clase que maneja todo el tema de la manzana
#Importamos los modulos necesarios
import pygame, os
from random import randint

class Manzana(pygame.sprite.Sprite):
	def __init__(self, dire, nombre, sw, sh):
		pygame.sprite.Sprite.__init__(self)
		#Cargo la imagen y creo el rectangulo de colision
		self.image = pygame.image.load(os.path.join(dire, nombre))
		self.rect = self.image.get_rect()
		self.rect.centerx = int(sw / 3)
		self.rect.centery = int(3 * sh / 4)
		self.colisiono = False

	def colision(self, viborita, sw, sh):
		#Reubico la manzana cuando es comida
		self.colisiono = True
		while self.colisiono:
			for bloque in range(0, viborita.long):
				if self.rect.colliderect(viborita.rect[0]):
					self.rect.centerx = randint(30, sw-30)
					self.rect.centery = randint(30, sh-30)
					self.colisiono = True
					break
				else:
					self.colisiono = False
			


	def dibujar(self, pantalla):
		pantalla.blit(self.image, (self.rect.centerx, self.rect.centery))

	