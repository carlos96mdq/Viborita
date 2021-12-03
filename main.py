#Main, donde inicia el programa
#Importamos los modulos necesarios
from stage import *

def main():
	#Inicializo las stages
	stages = Stage()
	#Bucle
	while True:
		#Seleccionar stage
		stages.stage_control()

if __name__ == '__main__':
	main()
