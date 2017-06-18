import pygame, sys, os
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
weight = 900
height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
tela = pygame.display.set_mode((weight, height))
pygame.display.set_caption("Jogo da cobrinha")
pygame.font.init()

time_moviment = 0
velocity_moviment = 500

tela.fill(WHITE)

class snake(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.ImageSnake = pygame.image.load('images/head.png')

        self.rect = self.ImageSnake.get_rect()
        self.rect.centerx = weight / 2
        self.rect.centery = height / 2

        self.size = 90

        self.life = True

    def put(self, surface):

        surface.blit(self.ImageSnake, self.rect)

def SnakeGame():

    player = snake()
    jogando = True
    direction = 1 # 1 - right || 2 - left || 3 - up || 4 - down

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT:

                    direction = 1

                if event.key == K_LEFT:

                    direction = 2

                if event.key == K_UP:

                    direction = 3

                if event.key == K_DOWN:

                    direction = 4

        player.put(tela)

        pygame.time.delay(velocity_moviment)

        pygame.display.update()


SnakeGame()