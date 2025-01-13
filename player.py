import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = pos

    def update(self):
        self.pos.x += 1
        self.rect.topleft = self.pos