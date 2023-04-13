import pygame
import sys

ancho= 300 #define el ancho de la pantalla
alto= 500 #define el alto de la pantalla
pygame.init() #iniciopyme
ventana=pygame.display.set_mode((ancho, alto)) #crea la ventana
pygame.display.set_caption("Proyecto.SAM") #asigna el nombre de la pantalla
ventana.fill([10,150,20])
while True:
    ventana.fill([10,200,18])
    for evento in pygame.event.get():
        print(evento)
        if evento.type==pygame.QUIT:
            sys.exit()
            
    pygame.display.update()