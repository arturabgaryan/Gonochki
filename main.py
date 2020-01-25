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

road = pygame.image.load("static/img/road.jpg")
# масштабируем картинку под размер экрана
road = scale(road, (1280, 1024))

left = False
right = False

left_2 = False
right_2 = False

car, car2 = Car(380, 800), SecondCar(780, 800)

# игровой цикл
while True:
    # обрабатываем события
    for e in pygame.event.get():
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
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")

    screen.blit(road, (0, 0))

    car.update(left, right)
    car.draw(screen)

    car2.update(left_2, right_2)
    car2.draw(screen)

    def fun():
        pass

    help_menu = pygameMenu.TextMenu(screen, 1280, 1024, font='static/fonts/Arial.ttf', title='Menu', bgfun=fun())
    help_menu.add_option('Simple button', fun, align=pygameMenu.locals.ALIGN_LEFT)
    help_menu.add_option('Return to Menu', pygameMenu.events.MENU_BACK)
    pygame.display.update()
