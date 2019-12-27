"""
Prueba del modulo pygame
Detecta el pasar del cursor sobre un circulo haciendolo cambiar de color
Al clickear sobre el circulo cambia a un color random
"""
import pygame
from pygame.locals import *
from sys import exit
from random import randint

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
random = (0,0,0)
color = white

pygame.init()

nombre_color = pygame.font.SysFont('arial', 20)
superf_texto = nombre_color.render('Blanco', True, (0,0,0))
superf_texto2 = nombre_color.render('Rojo', True, (0,0,0))
superf_texto3 = nombre_color.render('Random', True, (0,0,0))


window = pygame.display.set_mode((640, 480), 0, 32)

while True:
	window.fill((0,0,0))
	

	circle = pygame.draw.circle(window, color, (320,240),100)

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			if circle.collidepoint(pygame.mouse.get_pos()) == True:
				random = (randint(0,255),randint(0,255),randint(0,255))
				color = random

		
	if circle.collidepoint(pygame.mouse.get_pos()) == True and not color == random:
		color = red
			
	elif circle.collidepoint(pygame.mouse.get_pos()) == True and color == random:
		color = random
	else:
		color = white

	if color == white:
		window.blit(superf_texto,(320-superf_texto.get_width()/2,240-superf_texto.get_height()/2))
	elif color == red:
		window.blit(superf_texto2,(320-superf_texto2.get_width()/2,240-superf_texto2.get_height()/2))
	else:
		window.blit(superf_texto3,(320-superf_texto3.get_width()/2,240-superf_texto3.get_height()/2))




	pygame.display.update()
