import time
import pygame
import numpy as np
from random import randint

COLOUR_BG = (10,10,10)
COLOUR_GRID = (40,40,40)
COLOUR_DIE_NEXT = (170,170,170)
COLOUR_ALIVE_NEXT = (255,255,255)

def update(win, cells, size, with_prgress=False):
	update_cells = np.zeros((cells.shape[0], cells.shape[1]))

	for row, col in np.ndindex(cells.shape):
		alive_count = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
		colour = COLOUR_BG if cells[row, col] == 0 else COLOUR_ALIVE_NEXT

		if cells[row, col] == 1:
			if alive_count < 2 or alive_count > 3:
				if with_prgress:
					colour = COLOUR_DIE_NEXT
			elif 2 <= alive_count <= 3:
				update_cells[row, col] = 1
				if with_prgress:
					colour = COLOUR_ALIVE_NEXT
		else:
			if alive_count == 3:
				update_cells[row, col] = 1
				if with_prgress:
					colour = COLOUR_ALIVE_NEXT
		pygame.draw.rect(win, colour, (col * size, row * size, size -1 , size - 1))
	return update_cells

def main():
	pygame.init()
	win = pygame.display.set_mode((1000,1000))

	cells = np.zeros((100,100))
	win.fill(COLOUR_GRID)
	update(win, cells, 10)

	pygame.display.flip()
	pygame.display.update()

	running = False

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					running = not running
					update(win, cells, 10)
					pygame.display.update()
				if event.key == pygame.K_r:
					for cnt in range(1000):
						pos_x = randint(0, 999)
						pos_y = randint(0, 999)
						cells[pos_x//10, pos_y//10] = 1
					update(win,cells, 10)
					pygame.display.update()	
		
		win.fill(COLOUR_GRID)
		if running:
			cells = update(win, cells, 10, with_prgress=True)
			pygame.display.update()
		time.sleep(0.001)

if __name__ == '__main__':
	main()
