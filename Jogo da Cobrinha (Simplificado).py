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
size = 3

tela.fill(WHITE)

class snake(pygame.sprite.Sprite):



    def __init__(self):

        time = 0

        pygame.sprite.Sprite.__init__(self)
        self.ImageSnake = pygame.image.load('images2/corpo.png')

        self.rect = self.ImageSnake.get_rect()
        self.rect.centerx = weight / 2
        self.rect.centery = height / 2

        self.size = 90
        self.velocity = 20

        self.life = True

    def put(self, surface):

        surface.blit(self.ImageSnake, self.rect)

def SnakeGame():

    jogador = [snake(), snake(), snake()]
    player = snake()

    jogando = True
    direction = 1 # 1 - right || 2 - left || 3 - up || 4 - down

    pygame.mixer.music.load("Sounds/Game_Sound_2.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)

    while jogando == True:

        print("teste")
        pygame.time.delay(velocity_moviment)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT and direction != 2:

                    direction = 1

                if event.key == K_LEFT and direction != 1:

                    direction = 2

                if event.key == K_UP and direction != 4:

                    direction = 3

                if event.key == K_DOWN and direction != 3:

                    direction = 4

        if direction == 1:

            player.rect.right += player.velocity

        elif direction == 2:

            player.rect.left -= player.velocity

        elif direction == 3:

            player.rect.y -= player.velocity

        else:

            player.rect.y += player.velocity

        player.put(tela)

        pygame.display.update()


SnakeGame()