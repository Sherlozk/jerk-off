# -*- coding: utf-8 -*-
import pygame
from bullet import Bullet
from plane import Plane
from enemy import Enemy
from sys import exit

pygame.init()
screen = pygame.display.set_mode((449,799),0,24)
pygame.display.set_caption("jerk off!")
background = pygame.image.load('bg.jpg').convert()
bullets = []
score = 0
gameover = False
font = pygame.font.Font(None, 32)



def checkHit(enemy,bullet):
    if((bullet.x>enemy.x and bullet.x<enemy.x+enemy.image.get_width())and(bullet.y>enemy.y and bullet.y<enemy.y+enemy.image.get_height())):
        enemy.restart()
        bullet.active = False
        return True
    return False

def checkCrash(enemy, plane):
    if (plane.x + 0.7*plane.image.get_width() > enemy.x) and (plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + 0.7*plane.image.get_height() > enemy.y) and (plane.y + 0.3*plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False




for i in range(20):
    bullets.append(Bullet())

count_b = len(bullets)
index_b = 0
interval_b = 0
    
plane = Plane()

enemies = []
for i in range(10):
    enemies.append(Enemy())


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if not gameover:
        
        screen.blit(background,(0,0))

        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 1
            index_b = (index_b + 1) % count_b
    
        for b in bullets:
            if b.active:
                for e in enemies:
                    if checkHit(e, b):
                        score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))
    
        for e in enemies:
            if checkCrash(e,plane):
                gameover = True
            e.move()
            screen.blit(e.image,(e.x, e.y))
        
        plane.move()
        screen.blit(plane.image, (plane.x, plane.y))
        text = font.render("Score: %d" %score, 1, (0,0,0))
        screen.blit(text, (0, 0))
    else:
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False
        pass


            
    pygame.display.update()

    
