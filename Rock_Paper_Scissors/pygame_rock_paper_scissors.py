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

class SpriteSheet():
	def __init__(self, sheet, cols, rows):
		self.sheet = sheet
		self.cols = cols
		self.rows = rows
		self.total_cell_count = cols * rows

		self.rect = self.sheet.get_rect()
		w = self.cell_w = self.rect.width/cols
		h = self.cell_h = self.rect.height/rows
		hw, hh = self.cell_center = (w/2, h/2)

		self.cells = list([(index % cols * w, index//cols * h, w, h) for index in range(self.total_cell_count)])
		self.handle = list([
			(0,0), (-hw,0), (-w,0), 
			(0,-hh), (-hw,-hh), (-w,-hw), 
			(0,-h), (-hw,-h), (-h,-w)])

	def draw(self, surface, cell_index, x, y, handle=0):
		surface.blit(self.sheet, (x+self.handle[handle][0], y+self.handle[handle][1]), self.cells[cell_index])

sprite_file = pygame.image.load("EDITED_rpc_spritesheet.png")
print(type(sprite_file))
scale_sprite_test = pygame.transform.scale((sprite_file), (7*32*4, 6*32*4))
print(type(scale_sprite_test))

s = SpriteSheet(scale_sprite_test, 7, 6)

CENTER_HANDLE = 4
index = 0
index_timer = 0
index_update = 5

player_1 = Player(mode='player', color=(50, 50, 250), x=50, y=win_h/2-25, spd=5)
player_2 = Player(mode='player', color=(50, 175, 50), x=win_w-100, y=win_h/2-25, spd=5)

run = True
while run:
	clock.tick(FPS)

	win.fill((255, 255, 255))	

	s.draw(win, index % s.total_cell_count, player_1.x, player_1.y, CENTER_HANDLE)
	s.draw(win, index % s.total_cell_count, player_2.x, player_2.y, CENTER_HANDLE)

	index_timer += 1
	if index_timer >= index_update:
		index_timer = 0
		index += 1

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a] and player_1.x > player_1.spd:
		player_1.x -= player_1.spd
	if keys[pygame.K_d] and player_1.x < win_w - 50 - player_1.spd:
		player_1.x += player_1.spd
	if keys[pygame.K_w] and player_1.y > player_1.spd:
		player_1.y -= player_1.spd
	if keys[pygame.K_s] and player_1.y < win_h - 50 - player_1.spd:
		player_1.y += player_1.spd
 
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