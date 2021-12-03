#La clase que maneja el titulo del menu
#Importamos los modulos necesarios
import pygame, sys, os


class Menu:
    def __init__(self):
        # Se define la letra por defecto
        self.titulo_fuente = pygame.font.Font(None, 100)
        self.titulo_texto = "Super Viborita"
        self.titulo = self.titulo_fuente.render(self.titulo_texto, 1, (255, 255, 255))
        self.descripcion_fuente = pygame.font.Font(None, 40)
        self.descripcion_texto = "Presiones 'Espacio' para comenzar"
        self.descripcion = self.descripcion_fuente.render(self.descripcion_texto, 1, (255, 255, 255))

    def dibujar(self, pantalla, sw, sh):
        pantalla.blit(self.titulo, (sw/2 - 250, sh/2 - 200))
        pantalla.blit(self.descripcion, (sw / 2 - 250, sh / 2 - 50))