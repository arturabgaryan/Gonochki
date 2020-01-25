import pygame
import sys
import random
from pygame.transform import scale

class Car(pygame.sprite.Sprite):
    # конструктор - функция, в которую мы передаем начальные координаты
    def __init__(self, x, y):
        # инициализируем спрайт
        pygame.sprite.Sprite.__init__(self)

        # выбираем прямоугольную область размера 50 на 100
        self.rect = pygame.Rect(x, y, 50, 100)

        # загружаем картинку с кораблем
        self.image = scale(pygame.image.load("static/img/car.png"), (100, 170))

        # задаем начальную скорость по оси x
        self.xvel = 0

    # функция рисования корабля
    def draw(self, screen):
        # рисуем корабль на экране на месте занимаемой им прямоугольной области
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # функция перемещения, параметры - нажата ли стрелочки влево и вправо
    def update(self, left, right):
        # если нажата клавиша влево, уменьшаем скорость
        if left:
            self.xvel -= 6
        # если нажата клавиша вправо, увеличиваем скорость
        if right:
            self.xvel += 6
        # если ничего не нажато - тормозим
        if not (left or right):
            self.xvel = 0
        # изменяем координаты на скорость
        self.rect.x += self.xvel
