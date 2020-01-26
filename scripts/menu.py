import pygame
import sys

pygame.font.init()
window = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Archer')
menu = pygame.Surface((1280, 1024))
screen = pygame.Surface((1280, 1024))


class Menu:
    def __init__(self):
        self.captions = [(420, 100, u'Menu', (11, 0, 77), (250, 250, 30), 0, (None, 100))]
        self.punkts = [(420, 250, u'Play', (11, 0, 77), (250, 250, 30), 0, (None, 300)),
                  (420, 450, u'Exit', (11, 0, 77), (250, 250, 30), 1, (None, 300))]


    def render(self, poverhnost, num_punkt, p):
        punkts = p
        for i in punkts:
            font = pygame.font.Font(i[6][0], i[6][1])
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 300)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        menu.fill((0, 100, 200))
        screen.fill((0, 100, 200))
        self.render(screen, 2, self.captions)
        while done:


            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 255 and mp[1] > i[1] and mp[1] < i[1] + 150:
                    punkt = i[5]
            self.render(screen, punkt, self.punkts)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
            window.blit(menu, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()
            pygame.time.delay(5)



game = Menu()
game.menu()
