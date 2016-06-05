import pygame

class Plane:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.image = pygame.image.load('PaperPlane.png').convert_alpha()

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        self.x = mouseX - self.image.get_width()/2
        self.y = mouseY - self.image.get_height()/2

    def restart(self):
        self.x = 200
        self.y = 600
