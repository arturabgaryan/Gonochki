import pygame
import sys
import random
import time
from pygame.transform import scale
sys.path.append('scripts/')
from menu import Menu
from objects import Car, Coins, Explosion, Bushes


pygame.init()
pygame.font.init()
pygame.display.init()
window = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Archer')
menu = pygame.Surface((1280, 1024))


game = Menu()
game.menu()



# фон
gameover = scale(pygame.image.load('static/img/gameover.jpg'),(1280, 1024))
screen = pygame.display.set_mode((1280, 1024))
bg = scale(pygame.image.load('static/img/дорога.jpg').convert_alpha(), (1280, 1024))
screen.blit(bg, (0, 0))
screen.set_alpha(None)



# иконка
img = pygame.image.load('static/img/car.png').convert_alpha()
pygame.display.set_icon(img)

# fps
clock = pygame.time.Clock()
pygame.display.update()

# здесь определяются константы, классы и функции
x = 5
car = Car(200, 750, 'static/img/car.png')
car2 = Car(643, 750, 'static/img/car2.png')
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
f = 0
f2 = -1024

paused = True

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
        car.update(left, right, up, down, blocks, coins, type_car=0)
        car.draw(screen)
    if not car2.dead:
        car2.score += 1
        car2.update(left2, right2, up2, down2, blocks, coins, type_car=1)
        car2.draw(screen)

    for block in blocks:
        block.update()
        block.draw(screen)

    for coin in coins:
        coin.update(blocks)
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
