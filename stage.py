#Stage, donde se manejan las diferentes etapas del juego
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

class Stage:
    def __init__(self):
        #Indicamos el stage actual
        self.stage_actual = "Inicio"
        self.dt = 0

    #Inicializacion de la ventana
    def inicio(self):
        # Posiciono la ventana
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (S_X, S_Y)
        # Inicializo pygame
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.mixer.init()
        #Creo pantalla
        self.pantalla = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        pygame.display.set_caption("Viborita 2.0")
        #Se cargan los objetos
        self.fondo = Fondo(COLOR)
        self.viborita = Viborita(IMG_DIR, SON_DIR, "viborita.jpg", "viborita.ogg", S_WIDTH, S_HEIGHT)
        self.manzana = Manzana(IMG_DIR, "manzana.jpg", S_WIDTH, S_HEIGHT)
        self.menu = Menu()
        self.clock = pygame.time.Clock()
        #Adapto imagenes a la pantalla
        self.viborita.image = self.viborita.image.convert()
        self.manzana.image = self.manzana.image.convert()
        self.menu.titulo = self.menu.titulo.convert_alpha()
        #Designo la proxima Stage
        self.stage_actual = "Menu"

    def menu_principal(self):
        # Medir tiempo 60 fps
        self.dt = self.clock.tick(FPS)
        #Espero teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # La X de la ventana
                pygame.quit()
                sys.exit(0)
            # Controlo movimiento de viborita y salida del juego
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    # Designo la proxima Stage
                    self.stage_actual = "Escenario principal"
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
        # Dibujo el titulo
        self.fondo.dibujar(self.pantalla)
        self.menu.dibujar(self.pantalla, S_WIDTH, S_HEIGHT)
        pygame.display.flip()

    def escenaro_principal(self):
        # Medir tiempo 60 fps
        self.dt = self.clock.tick(FPS)
        # Actualizamos objetos en pantalla
        self.viborita.update(self.dt, S_WIDTH, S_HEIGHT)
        # Vemos si hubo colision
        self.viborita.colision(self.manzana)
        self.manzana.colision(self.viborita, S_WIDTH, S_HEIGHT)
        # Manejo de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # La X de la ventana
                sys.exit(0)
            # Controlo movimiento de viborita y salida del juego
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
        # Actualizamos pantalla
        self.fondo.dibujar(self.pantalla)
        self.manzana.dibujar(self.pantalla)
        self.viborita.dibujar(self.pantalla)
        pygame.display.flip()

    def stage_control(self):
       if self.stage_actual == "Inicio" :
           self.inicio()
       elif self.stage_actual == "Menu":
           self.menu_principal()
       elif self.stage_actual == "Escenario principal" :
           self.escenaro_principal()



