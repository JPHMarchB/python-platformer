import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from pygame.sprite import _Group
pygame.init()

pygame.display.set_caption('Pixel Jumper')

WIDTH, HEIGHT = 1000, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # Player moves left
    def move_left(self, vel):
        self.x_vel = -vel

        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    # Player moves right
    def move_right(self, vel):
        self.x_vel = vel

        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
        




# Background display function
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


# Draw function
def draw(window, background, bg_image):

    # Background display
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


# Main functionality
def main(window):
    clock = pygame.time.Clock()

    # Background color selector
    background, bg_image = get_background("Pink.png")

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)


    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)