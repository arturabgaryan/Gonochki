import pygame
import sys
import random
import time
from pygame.transform import scale

pygame.init()
# фон
gameover = scale(pygame.image.load('Game_over.jpg'),(1024,904))
screen = pygame.display.set_mode((1024, 904))
bg = pygame.image.load('doroga1.jpg').convert_alpha()
screen.blit(bg, (0, 0))
screen.set_alpha(None)

# иконка
img = pygame.image.load('car.png').convert_alpha()
pygame.display.set_icon(img)

# fps
clock = pygame.time.Clock()
pygame.display.update()

# здесь определяются константы, классы и функции
class Coins(pygame.sprite.Sprite):
     def __init__(self,x,y,speed):
         pygame.sprite.Sprite.__init__(self)
         self.image = scale(pygame.image.load('coin.png').convert_alpha(),(50, 50))
         self.rect = pygame.Rect(x, y, 50, 50)
         self.yvel = speed

     def draw(self, screen):
         screen.blit(self.image, (self.rect.x, self.rect.y))

     def update(self):
         self.rect.y += self.yvel

         if self.rect.y > 900:
             self.kill()

         for block in blocks:
             if self.rect.colliderect(block.rect):
                 self.kill()



class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.images = []
        self.index = 0

        for i in range(8):
            image = scale(pygame.image.load(f"tile00{i}.png").convert_alpha(), (100, 100))
            self.images.append(image)

    def draw(self, screen):
        if self.index < 8:
            screen.blit(self.images[self.index], (self.rect.x, self.rect.y))
            self.index += 1


class Bushes(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        img1 = scale(pygame.image.load("rock.png").convert_alpha(), (50, 100))
        img2 = scale(pygame.image.load("bush.png").convert_alpha(), (50, 100))
        img3 = scale(pygame.image.load("box.png").convert_alpha(), (50, 100))
        imgs = [img1, img2,img3]
        self.image = scale(random.choice(imgs), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()

x = 5
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.img_car = [pygame.image.load(img).convert_alpha(),pygame.image.load('car_left.png').convert_alpha(),pygame.image.load('car_right.png').convert_alpha()]
        self.img_car2 = [pygame.image.load(img).convert_alpha(), pygame.image.load('car2_left.png').convert_alpha(), pygame.image.load('car2_right.png').convert_alpha()]
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = scale(pygame.image.load(img).convert_alpha(), (50, 100)).convert_alpha()
        self.xvel = 0
        self.yvel = 0
        self.life = 5
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
                if self == car:
                    self.image = scale(self.img_car[0], (50, 100))
                else:
                    self.image = scale(self.img_car2[0], (50, 100))
                self.xvel = 0
            else:
                if self == car:
                    self.image = scale(self.img_car[1], (50, 100))
                else:
                    self.image = scale(self.img_car2[1], (50, 100))
                self.xvel = -5

        if right:
            if self.rect.x > 933:
                if self == car:
                    self.image = scale(self.img_car[0], (50, 100))
                else:
                    self.image = scale(self.img_car2[0], (50, 100))
                self.xvel = 0
            else:
                if self == car:
                    self.image = scale(self.img_car[2], (50, 100))
                else:
                    self.image = scale(self.img_car2[2], (50, 100))
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
            if self == car:
                self.image = scale(self.img_car[0], (50, 100))
            else:
                self.image = scale(self.img_car2[0], (50, 100))
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
        for coin in coins:
            if self.rect.colliderect(coin.rect):
                coin.kill()
                self.score += 300



car = Car(200, 750, 'car.png')
car2 = Car(643, 750, 'car2.png')
speed = 10
left = False
right = False
up = False
down = False
left2 = False
right2 = False
up2 = False
down2 = False
coins =  pygame.sprite.Group()
blocks = pygame.sprite.Group()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
f =0
f2 = -1024
while True:
    screen.blit(bg, (0, f))
    screen.blit(bg, (0, f2))
    if (car.score%1000 == 0) or (car2.score%1000 == 0):
        speed += 2
    f +=  speed
    f2 +=  speed
    if f > 800:
        f = -1024
    if f2 > 800:
        f2 = -1024
    clock.tick(60)
    if random.randint(1, 1000) > 960:
        block_x = random.randint(90, 920)
        block_y = -10
        block = Bushes(block_x, block_y,speed)
        blocks.add(block)
    if random.randint(1, 1000) > 990:
        coin_x = random.randint(90, 920)
        coin_y = -10
        coin = Coins(coin_x, coin_y,speed)
        coins.add(coin)
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

    for coin in coins:
        coin.update()
        coin.draw(screen)

    life = font.render(f'RED_LIFE: {car.life}', False, (0, 255, 255))
    life2 = font.render(f'BLUE_LIFE: {car2.life}', False, (0, 255, 255))
    score = font.render(f'RED_SCORE: {car.score}', False, (0, 255, 255))
    score2 = font.render(f'BLUE_SCORE: {car2.score}', False, (0, 255, 255))

    if car.dead and car2.dead:
        screen.blit(gameover,(0,0))
        if car.score > car2.score:
            screen.blit(score, (400, 700))
            screen.blit(score2, (400, 800))
        else:
            screen.blit(score2, (400, 800))
            screen.blit(score, (400, 700))

        pygame.display.update()
        time.sleep(10)
        pygame.quit()
    else:
        screen.blit(life, (20, 20))
        screen.blit(life2, (820, 20))
        screen.blit(score, (20, 60))
        screen.blit(score2, (820, 60))


    pygame.display.update()