#TOCANDO MUSICA NO PYTHON
import pygame
pygame.mixer.init()
pygame.init() #É NECESSÁRIO TAMBÉM ESTE COMANDO
pygame.mixer.music.load('osg057.mp3')
pygame.mixer.music.play()
pygame.event.wait()
