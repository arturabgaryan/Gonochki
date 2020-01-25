import pygame
import sys
import random
from pygame.transform import scale
sys.path.append("scripts/")

from objects import Car
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

car = Car(300, 850)

# игровой цикл
while True:
    # обрабатываем события
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True

        # если отпущена клавиша - меняем переменную
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False
        # если нажали на крестик
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")

    screen.blit(road, (0, 0))

    car.update(left, right)
    car.draw(screen)
    pygame.display.update()
