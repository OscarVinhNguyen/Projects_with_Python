"""
Rock, Paper, Scissor, Shoot   (w/ PYGAME)
Made by Oscar-Vinh Nguyen
07/20/2020
"""



import pygame
import time

win_w = 1280
win_h = 756
win = pygame.display.set_mode((win_w, win_h))

pygame.display.set_caption("Rock, Paper, Scissors, Shoot")

FPS = 60 # 60 frames per second
clock = pygame.time.Clock()

class Player():

	def __init__(self, mode, color, x, y, spd):
		self.mode = mode # "player" or "computer"
		self.color = color
		self.x = x
		self.y = y
		self. spd = spd

player_1 = Player(mode='player', color=(50, 50, 250), x=50, y=win_h/2-25, spd=5)
player_2 = Player(mode='player', color=(50, 175, 50), x=win_w-100, y=win_h/2-25, spd=5)

run = True
while run:
	clock.tick(FPS)

	win.fill((255, 255, 255))	

	pygame.draw.rect(win, player_1.color, (player_1.x, player_1.y, 50, 50))
	pygame.draw.rect(win, (255, 255, 255), (player_1.x+10, player_1.y+10, 30, 30))

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a] and player_1.x > player_1.spd:
		player_1.x -= player_1.spd
	if keys[pygame.K_d] and player_1.x < win_w - 50 - player_1.spd:
		player_1.x += player_1.spd
	if keys[pygame.K_w] and player_1.y > player_1.spd:
		player_1.y -= player_1.spd
	if keys[pygame.K_s] and player_1.y < win_h - 50 - player_1.spd:
		player_1.y += player_1.spd

	pygame.draw.rect(win, player_2.color, (player_2.x, player_2.y, 50, 50))
	pygame.draw.rect(win, (255, 255, 255), (player_2.x+10, player_2.y+10, 30, 30))
 
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player_2.x > player_2.spd:
		player_2.x -= player_2.spd
	if keys[pygame.K_RIGHT] and player_2.x < win_w - 50 - player_2.spd:
		player_2.x += player_2.spd
	if keys[pygame.K_UP] and player_2.y > player_2.spd:
		player_2.y -= player_2.spd
	if keys[pygame.K_DOWN] and player_2.y < win_h - 50 - player_2.spd:
		player_2.y += player_2.spd

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()