import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.circle(screen,[255,0,0],[80,80],30,0)
pygame.display.flip()
background_image_filename = "123.jpg"
while True:
    for event in pygame.event.get():
        if event.type == pyagame.QUIT:
            sys.exit()
