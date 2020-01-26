import pygame
import sys
import random
import time
from pygame.transform import scale


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.img_car = [pygame.image.load(img).convert_alpha(),pygame.image.load('../static/ar_left.png').convert_alpha(),pygame.image.load('../static/car_right.png').convert_alpha()]
        self.img_car2 = [pygame.image.load(img).convert_alpha(), pygame.image.load('../static/car2_left.png').convert_alpha(), pygame.image.load('../static/car2_right.png').convert_alpha()]
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

class Coins(pygame.sprite.Sprite):
     def __init__(self,x,y,speed):
         pygame.sprite.Sprite.__init__(self)
         self.image = scale(pygame.image.load('../static/coin.png').convert_alpha(),(50, 50))
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
            image = scale(pygame.image.load(f"../static/tile00{i}.png").convert_alpha(), (100, 100))
            self.images.append(image)

    def draw(self, screen):
        if self.index < 8:
            screen.blit(self.images[self.index], (self.rect.x, self.rect.y))
            self.index += 1


class Bushes(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        img1 = scale(pygame.image.load("../static/rock.png").convert_alpha(), (50, 100))
        img2 = scale(pygame.image.load("../static/bush.png").convert_alpha(), (50, 100))
        img3 = scale(pygame.image.load("../static/box.png").convert_alpha(), (50, 100))
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
