#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import sys
 
# здесь определяются константы, классы и функции
FPS = 120
 
pygame.init()
screen = pygame.display.set_mode((1024, 904))
bg = pygame.image.load('doroga1.jpg')
screen.blit(bg, (0, 0))
img = pygame.image.load('car_icon.jpg')
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.display.update()
x = 200
BLUE = (0, 70, 225)
# главный цикл
while True:
    screen = pygame.display.set_mode((1024, 904))
    bg = pygame.image.load('doroga1.jpg')
    screen.blit(bg, (0, 0))
    clock.tick(FPS)
    pygame.draw.circle(screen, BLUE, (x, 700), 40)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            if x <= 104:
                x += 0
            else:
                x -= 15
        
        elif keys[pygame.K_RIGHT]:
            if x >= 443:
                x += 0
            else:
                x += 15
    pygame.display.update()


# In[ ]:





# In[ ]:




