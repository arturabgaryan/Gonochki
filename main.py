import pygame
from random import randint
import sys
FPS = 120

pygame.init()
screen = pygame.display.set_mode((1024, 600))
bg = pygame.image.load('static/дорога.jpg')
screen.blit(bg, (0, 0))
# img = pygame.image.load('cards.png')
# pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.display.update()
x = 200
BLUE = (0, 70, 225)

objects = []
objects.append({'x':randint(),'y':0})
# главный цикл
while True:
    screen = pygame.display.set_mode((1024, 600))
    bg = pygame.image.load('static/дорога.jpg')
    screen.blit(bg, (0, 0))
    clock.tick(FPS)
    pygame.draw.circle(screen, BLUE, (x, 500), 40)
    for object in objects:
        pygame.draw.rect(screen, (255, 0, 0), (200,object['y'],200,100))
        object['y']+=10
        if object['y'] <=0:
            objects.remove(object)
    print(objects)
    #objects.append({'y':0})
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if x == 0:
                pass
            else:
                x -= 15

        elif keys[pygame.K_RIGHT]:
            x += 15
    pygame.display.update()
