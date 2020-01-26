import pygame
import sys
import random
import time
from pygame.transform import scale

pygame.init()
# фон
screen = pygame.display.set_mode((1024, 904))
bg = pygame.image.load('static/img/дорога.jpg')
screen.blit(bg, (0, 0))

# иконка
img = pygame.image.load('static/img/car.png')
pygame.display.set_icon(img)

# fps
clock = pygame.time.Clock()
pygame.display.update()

# здесь определяются константы, классы и функции


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.images = []
        self.index = 0

        for i in range(8):
            image = scale(pygame.image.load(f"tile00{i}.png"), (100, 100))
            self.images.append(image)

    def draw(self, screen):
        if self.index < 8:
            screen.blit(self.images[self.index], (self.rect.x, self.rect.y))
            self.index += 1


class Bushes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img1 = scale(pygame.image.load("static/img/rock.png"), (50, 100))
        img2 = scale(pygame.image.load("static/img/bush.png"), (50, 100))
        img3 = scale(pygame.image.load("static/img/box.png"), (50, 100))
        imgs = [img1, img2,img3]
        self.image = scale(random.choice(imgs), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = scale(pygame.image.load(img), (50, 100))
        self.xvel = 0
        self.yvel = 0
        self.life = 1
        self.dead = False
        self.score = 0
        self.explosions = []

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        for explosion in self.explosions:
            explosion.draw(screen)

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

        for block in blocks:
            if self.life == 0:
                self.dead = True
            elif self.rect.colliderect(block.rect):
                self.life -= 1
                rx = random.randint(-5, 40)
                ry = random.randint(-5, 40)
                explosion = Explosion(self.rect.x + rx, self.rect.y + ry)
                self.explosions.append(explosion)
                block.kill()


car = Car(200, 750, 'static/img/car.png')
car2 = Car(643, 750, 'static/img/car2.png')

left = False
right = False
up = False
down = False
left2 = False
right2 = False
up2 = False
down2 = False

blocks = pygame.sprite.Group()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
f =0
f2 = -1024
while True:
    screen.blit(bg, (0, f))
    screen.blit(bg, (0, f2))
    f += 7
    f2 += 7
    if f > 800:
        f = -1024
    if f2 > 800:
        f2 = -1024
    clock.tick(60)
    if random.randint(1, 1000) > 970:
        block_x = random.randint(90, 920)
        block_y = -100
        block = Bushes(block_x, block_y)
        blocks.add(block)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            left = True
            right = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            right = True
            left = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            up = True
            down = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            down = True
            up = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left2 = True
            right2 = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right2 = True
            left2 = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up2 = True
            down2 = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            down2 = True
            up2 = False

        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_d:
            right = False
        if e.type == pygame.KEYUP and e.key == pygame.K_w:
            up = False
        if e.type == pygame.KEYUP and e.key == pygame.K_s:
            down = False

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            down2 = False

        elif e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not car.dead:
        car.score += 1
        car.update(left, right, up, down, blocks)
        car.draw(screen)
    if not car2.dead:
        car2.score += 1
        car2.update(left2, right2, up2, down2, blocks)
        car2.draw(screen)

    for block in blocks:
        block.update()
        block.draw(screen)

    life = font.render(f'RED_LIFE: {car.life}', False, (0, 255, 255))
    life2 = font.render(f'BLUE_LIFE: {car2.life}', False, (0, 255, 255))
    score = font.render(f'RED_SCORE: {car.score}', False, (0, 255, 255))
    score2 = font.render(f'BLUE_SCORE: {car2.score}', False, (0, 255, 255))
    screen.blit(life, (20, 20))
    screen.blit(life2, (880, 20))
    screen.blit(score, (20, 60))
    screen.blit(score2, (880, 60))
    if car.dead and car2.dead:
        screen.blit(score, (400, 200))
        screen.blit(score2, (400, 400))
        pygame.display.update()
        time.sleep(10)
        pygame.quit()

    pygame.display.update()
