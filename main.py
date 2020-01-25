<<<<<<< HEAD
# #!/usr/bin/env python
# # coding: utf-8
# import pygameMenu
# from pygameMenu.locals import *
# import pygame
# import sys
#
# # здесь определяются константы, классы и функции
# FPS = 120
# in_game = False
# paused = False
#
#
# pygame.init()
# screen = pygame.display.set_mode((1024, 1280))
# bg = pygame.image.load('road.jpg')
# screen.blit(bg, (0, 0))
# #img = pygame.image.load('cards.png')
# # pygame.display.set_icon(img)
# clock = pygame.time.Clock()
# pygame.display.update()
# x = 200
# BLUE = (0, 70, 225)
#
# def draw_bg():
#     screen.blit(bg, (0, 0))
#
#
# def init_menu():
#     global screen
#     menu = pygameMenu.Menu(screen,
#                     title="Settings",
#
#                     font="static/fonts/Arial.ttf",
#                     font_size=60,
#
#                     window_width=1024,
#                     window_height=1280,
#
#                     bgfun=draw_bg,
#
#                     menu_color=(255, 255, 255),
#                     color_selected=(50, 50, 50),
#                     font_color=(0, 0, 0),
#                     option_shadow=False)
#     return menu
#
#
# menu = init_menu()
#
#
#
# # главный цикл
# while True:
#     screen = pygame.display.set_mode((1024, 1280))
#     bg = pygame.image.load('road.jpg')
#     screen.blit(bg, (0, 0))
#     clock.tick(FPS)
#     pygame.draw.circle(screen, BLUE, (x, 700), 40)
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_LEFT]:
#             if x == 0:
#                 pass
#             else:
#                 x -= 15
#
#         elif keys[pygame.K_RIGHT]:
#             x += 15
#     if in_game and not paused:
#         pygame.mixer.music.stop()
#         in_game = field.tick(pressed, space, keys)
#     else:
#         menu.draw(events)
#     pygame.display.update()
=======
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
>>>>>>> 6098b874f55f77ba8a3fdb3ac5d1f918588d77de
