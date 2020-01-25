import pygame
import sys
from pygame.transform import scale
sys.path.append("scripts/")

from cars import Car
pygame.init()

# создаем окно размера 800 на 600
screen = pygame.display.set_mode((1280, 1024))

# указываем название
pygame.display.set_caption("RaceMode")

road = pygame.image.load("static/img/road.jpg")
# масштабируем картинку под размер экрана
road = scale(road, (1280, 1024))

car = Car(400, 400)

# игровой цикл
while True:
    # обрабатываем события
    for e in pygame.event.get():
        # если нажали на крестик
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")
    car.draw(screen)
    screen.blit(road, (0, 0))
    pygame.display.update()
