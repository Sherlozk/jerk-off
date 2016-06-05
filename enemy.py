import pygame
from random import randint
from random import random

class Enemy:
    def __init__(self):
        self.x = randint(0, 400)
        self.y = randint(-500, 0)
        self.speed = 1
        self.image = pygame.image.load('enemy.png').convert_alpha()

    def restart(self):
        self.x = randint(0, 400)
        self.y = randint(-500, 0)
        if self.speed < 20:
            self.speed += 0.05


    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()
        
    
