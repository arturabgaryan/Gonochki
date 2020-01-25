import pygame
import sys
import random
import pygameMenu
from pygame.transform import scale
sys.path.append("scripts/")
from objects import Car, SecondCar
pygame.init()

# создаем окно размера 800 на 600
screen = pygame.display.set_mode((1280, 1024))

# указываем название
pygame.display.set_caption("RaceMode")
# масштабируем картинку под размер экрана
road = scale(pygame.image.load("static/img/road.jpg"), (1280, 1024))
menu_bg = scale(pygame.image.load('static/img/menu_bg.jpg'), (1280, 1024))

left = False
right = False

left_2 = False
right_2 = False

car, car2 = Car(380, 800), SecondCar(780, 800)


def draw_bg():
    pass


def printout():
    global pause
    print(44)
    pause = False


# игровой цикл
pause = True
in_game = False

help_menu = pygameMenu.TextMenu(screen, window_width=1280, window_height=1024, font='static/fonts/Arial.ttf', title='RaceMode', bgfun=draw_bg, color_selected=(255, 255, 255), draw_select=True)

help_menu.add_option('Start', pygameMenu.events.CLOSE)
help_menu.add_option('Exit', pygameMenu.events.EXIT)

while True:
    # обрабатываем события
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")
        else:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left_2 = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right_2 = True

            # если отпущена клавиша - меняем переменную
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left_2 = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right_2 = False
            if e.type == pygame.KEYUP and e.key == pygame.K_a:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_d:
                right = False


        # если нажали на крестик


    if pause == False:
        print(pause)
        screen.blit(road, (0, 0))

        car.update(left, right)
        car.draw(screen)

        car2.update(left_2, right_2)
        car2.draw(screen)
    else:
        screen.blit(menu_bg, (0, 0))
        help_menu.draw()
        print(help_menu.is_disabled())
    pygame.display.update()
