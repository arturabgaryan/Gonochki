import pygame
import sys
import random
from pygame.transform import scale
import pandas as pd
import pickle

pygame.init()
# фон
screen = pygame.display.set_mode((1024, 904))
bg = pygame.image.load('/Users/tikhon/Desktop/Gonochki/static/img/дорога.jpg')
screen.blit(bg, (0, 0))

# иконка
img = pygame.image.load('/Users/tikhon/Desktop/Gonochki/static/img/car.png')
pygame.display.set_icon(img)

# fps
clock = pygame.time.Clock()
pygame.display.update()

# здесь определяются константы, классы и функции


class Bushes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img1 = scale(pygame.image.load(
            "/Users/tikhon/Desktop/Gonochki/static/img/rock.png"), (50, 100))
        img2 = scale(pygame.image.load(
            "/Users/tikhon/Desktop/Gonochki/static/img/bush.png"), (50, 100))
        imgs = [img1, img2]
        self.image = scale(random.choice(imgs), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()


class Lines(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (250, 250, 10, 300))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 1000:
            self.kill()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = scale(pygame.image.load(img), (50, 100))
        self.xvel = 0
        self.yvel = 0
        # добавим кораблю здоровье
        self.life = 5
        self.dead = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left, right, up, down, asteroids):
        if left:
            if self.rect.x < 80:
                self.xvel = 0
            else:
                self.xvel = -5

        if right:
            if self.rect.x > 933:
                self.xvel = 0
            else:
                self.xvel = 5

        if up:
            if self.rect.y < 80:
                self.yvel = 0
            else:
                self.yvel = -5

        if down:
            if self.rect.y > 703:
                self.yvel = 0
            else:
                self.yvel = 5

        if not (left or right or up or down):
            self.xvel = 0
            if self.rect.y > 703:
                self.yvel = 0
            else:
                self.yvel = 3
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.life == 0:
                self.dead = True
            elif self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                self.life -= 1
                asteroid.kill()


car = Car(200, 750, '/Users/tikhon/Desktop/Gonochki/static/img/car.png')
car2 = Car(643, 750, '/Users/tikhon/Desktop/Gonochki/static/img/car2.png')
left = False
right = False
up = False
down = False
left2 = False
right2 = False
up2 = False
down2 = False
asteroids = pygame.sprite.Group()
# загрузим системный шрифт
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
# главный цикл

data = []


def savedata(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


while True:
    d = {}
    screen.blit(bg, (0, 0))
    clock.tick(60)
    if random.randint(1, 1000) > 970:
        asteroid_x = random.randint(90, 920)
        asteroid_y = -100
        asteroid = Bushes(asteroid_x, asteroid_y)
        asteroids.add(asteroid)

    i = 0
    for asteroid in asteroids:
        d[str(i)] = {"x": asteroid.rect.x, "y": asteroid.rect.y}
        i += 1
    d["car"] = {"x": car.rect.x, "y": car.rect.y}

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            d['act'] = {'k': 'a', 'act': 1}
            left = True
            right = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            d['act'] = {'k': 'd', 'act': 1}
            right = True
            left = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            d['act'] = {'k': 'w', 'act': 1}
            up = True
            down = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            d['act'] = {'k': 's', 'act': 1}
            down = True
            up = False

        elif e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            d['act'] = {'k': 'LEFT', 'act': 1}
            left2 = True
            right2 = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            d['act'] = {'k': 'RIGHT', 'act': 1}
            right2 = True
            left2 = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            d['act'] = {'k': 'UP', 'act': 1}
            up2 = True
            down2 = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            d['act'] = {'k': 'DOWN', 'act': 1}
            down2 = True
            up2 = False

        elif e.type == pygame.KEYUP and e.key == pygame.K_a:
            d['act'] = {'k': 'a', 'act': 0}
            left = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_d:
            d['act'] = {'k': 'd', 'act': 0}
            right = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_w:
            d['act'] = {'k': 'w', 'act': 0}
            up = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_s:
            d['act'] = {'k': 's', 'act': 0}
            down = False

        elif e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            d['act'] = {'k': 'LEFT', 'act': 0}
            left2 = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            d['act'] = {'k': 'RIGHT', 'act': 0}
            right2 = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_UP:
            d['act'] = {'k': 'UP', 'act': 0}
            up2 = False
        elif e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            d['act'] = {'k': 'DOWN', 'act': 0}
            down2 = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_x:
            savedata(data, 'data')

        elif e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        else:
            d['act'] = None
    print(d)
    data.append(d)
    car.update(left, right, up, down, asteroids)
    car.draw(screen)
    car2.update(left2, right2, up2, down2, asteroids)
    car2.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)

    # выведем жизнь на экран белым цветом
    life = font.render(f'LIFE: {car.life}', False, (0, 255, 255))
    life = font.render(f'LIFE2: {car2.life}', False, (0, 255, 255))
    screen.blit(life, (20, 20))
    if car.dead == True:
        savedata(data, 'data')
        pygame.quit()

    elif car2.dead == True:
        savedata(data, 'data')
        pygame.quit()

    pygame.display.update()
