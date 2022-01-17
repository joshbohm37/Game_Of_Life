import math
import sys

import config


import pygame
from pygame.locals import *

from button import Button
from cell import Cell

from grid import gen_grid, gen_grid_sprites, update_grid


from sys import exit

pygame.init()

vec = pygame.math.Vector2

resolution = pygame.display.Info()
screen = pygame.display.set_mode((resolution.current_w, resolution.current_h), flags=pygame.FULLSCREEN|pygame.SCALED)

screen_w = screen.get_width()
screen_h = screen.get_height()


FPS = 60
clock = pygame.time.Clock()

grid_size = config.grid_size
grid_padding = config.grid_padding
cell_size = config.cell_size
grid_width = config.grid_width
global_center = config.global_center
grid_top_left = config.grid_top_left


rect_group = pygame.sprite.Group()
starting_grid = gen_grid(grid_size)

gen_grid_sprites(grid_size, starting_grid, rect_group)


new_generation = pygame.USEREVENT + 1
generation_time = 50
pygame.time.set_timer(new_generation, generation_time)

PAUSE = True
SHOW_GRID = True

#BACKGROUND GRID CODE#
background_grid = pygame.sprite.Sprite()
background_grid.surf = pygame.Surface((grid_width+4, grid_width+4))
background_grid.surf.fill((128, 128, 128))
background_grid.rect = background_grid.surf.get_rect(center = (global_center[0] - 1, global_center[1] - 1))

button = Button((1250, 1000), (100, 50), "SUCK DEEZ")
button_group = pygame.sprite.Group()
button_group.add(button)


def quit():
    pygame.quit()
    sys.exit()


def draw(entity):
    screen.blit(entity.surf, entity.rect)


while True:
    screen.fill((0, 0, 0))
    if SHOW_GRID:
        draw(background_grid)


    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_SPACE:
                PAUSE = not PAUSE

            if event.key == pygame.K_g:
                SHOW_GRID = not SHOW_GRID
        if not PAUSE:
            if event.type == new_generation:
                for entity in rect_group:
                    entity.kill()

                starting_grid = update_grid(starting_grid)
                gen_grid_sprites(grid_size, starting_grid, rect_group)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] < (global_center[0]+(grid_width/2)) and event.pos[0] > (global_center[0]-(grid_width/2))) and (event.pos[1] > (global_center[1]-(grid_width/2)) and event.pos[1] < (global_center[1]+(grid_width/2))):
                for entity in rect_group:
                    if entity.check_click(event.pos):

                        cellrow = math.ceil((entity.rect.topleft[1] - grid_top_left[1])/(cell_size + grid_padding))
                        cellcol = math.ceil((entity.rect.topleft[0] - grid_top_left[0])/(cell_size + grid_padding))
                        
                        if starting_grid[cellrow][cellcol] == 1:
                            entity.surf.fill((0,0,0))
                            starting_grid[cellrow][cellcol] = 0
                        elif starting_grid[cellrow][cellcol] == 0:
                            entity.surf.fill((255,255,255))
                            starting_grid[cellrow][cellcol] = 1

    for entity in rect_group:
        draw(entity)

    for entity in button_group:
        entity.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


