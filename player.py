import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos: pygame.Vector2, move_speed: float):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = pos
        self.move_speed = move_speed

    def update(self, inputs):
        self.move(inputs)

    def move(self, inputs):
        horizontal_move = (inputs[pygame.K_d] + inputs[pygame.K_RIGHT]) - (inputs[pygame.K_a] + inputs[pygame.K_LEFT])
        vertical_move = (inputs[pygame.K_s] + inputs[pygame.K_DOWN]) - (inputs[pygame.K_w] + inputs[pygame.K_UP])
        
        move_vector = pygame.Vector2(horizontal_move, vertical_move)
        if move_vector.x != 0 or move_vector.y != 0:
            move_vector.scale_to_length(self.move_speed)
        self.pos += move_vector
        self.rect.topleft = self.pos
        print(move_vector)