import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1024, 904))
bg = pygame.image.load('static/дорога.jpg')
screen.blit(bg, (0, 0))
#фон

img = pygame.image.load('car_icon.jpg')
pygame.display.set_icon(img)
#иконка

clock = pygame.time.Clock()
pygame.display.update()
# здесь определяются константы, классы и функции

x = 200
X = 200
Y = -40
BLUE = (0, 70, 225)
COL = (123,42,63)
counter = 1
const = 200
FPS = 120

class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

# главный цикл
while True:
    screen = pygame.display.set_mode((1024, 904))
    bg = pygame.image.load('static/дорога.jpg')
    screen.blit(bg, (0, 0))
    clock.tick(FPS)
    pygame.draw.circle(screen, BLUE, (x, 700), 40)
    for i in range(counter):
        pygame.draw.circle(screen, COL, (X, Y), 40)
        X = X+120
    X = const
    Y += 15
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if x <= 104:
                x += 0
            else:
                x -= 15

        elif keys[pygame.K_d]:
            if x >= 443:
                x += 0
            else:
                x += 15
    if Y >= 944:
        Y = -40
        X += 150
        if counter == 1:
            counter = 1
        else:
            counter += 0
        const = random.randint(100,443)
        const += 40
        X = const
    pygame.display.update()
