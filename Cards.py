import pygame
import sys

pygame.init()
land = pygame.image.load("стол.jpg")
land = pygame.transform.scale(land, (800, 600))
SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Card Game")
screen.blit(land, (0, 0))


class Card (pygame.sprite.Sprite):

    def __init__(self,image, x, y, force):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(image), (80,130))
        self.rect = self.image.get_rect()
        self.force = force

