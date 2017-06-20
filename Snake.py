import pygame, os, sys, random, time
from pygame.locals import *

pygame.init()

# ------------ pattern general configurations ------------ #

os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 900
height = 600
display = pygame.display.set_mode((width, height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [WHITE, BLACK, RED, GREEN, BLUE]

pygame.display.set_caption("Jogo da cobrinha")
pygame.font.init()
font = pygame.font.SysFont(None, 25)

display.fill(BLACK)
block_size = 10

clock = pygame.time.Clock()

# ------------ pattern general configurations ------------ #

def making_snake(snakelist):

    for pos_x_y in snakelist:
        pygame.draw.rect(display, GREEN, [pos_x_y[0], pos_x_y[1], block_size, block_size]) # Create a block with the two firsts parameters being the position and the others two being the size

def message_to_screen (message, color, pos_x, pos_y):

    screen_text = font.render(message, True, color)
    display.blit(screen_text, [pos_x, pos_y])

def SnakeGame ():

    # ------------ pattern game configurations ------------ #

    pygame.mixer.music.load("Sounds/Game_Sound_2.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)

    position_x = width / 2
    position_y = height / 2
    direction_x = 0
    direction_y = 0

    no_apple_in_screen = True

    difficult = 5
    playing = True
    game_over = False

    limit_colors = 170

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    first_body = False
    apple_tam = 3
    apple_parameter = apple_tam

    snake_body = []

    # ------------ pattern game configurations ------------ #

    while playing:

        while no_apple_in_screen:

            apple_x = random.randrange(0, width / 10) * block_size
            apple_y = random.randrange(0, height / 10) * block_size
            apple_location = [apple_x, apple_y]

            blank_position = True

            for snake_body_lenght in snake_body:

                if snake_body_lenght == apple_location:

                    blank_position = False

            if blank_position:

                no_apple_in_screen = False

        while game_over:

            pygame.mixer.music.set_volume(0)
            display.fill(WHITE)
            message_to_screen("Game Over, press P to play again or Q to quit", BLACK, width/2 - 170, height/2)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q or event.type == pygame.QUIT:

                        playing = False
                        game_over = False

                    elif event.key == pygame.K_p:

                        SnakeGame()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                playing == False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and direction_x != block_size:
                    direction_x = -block_size
                    direction_y = 0

                elif event.key == pygame.K_RIGHT and direction_x != -block_size:
                    direction_x = block_size
                    direction_y = 0

                elif event.key == pygame.K_UP and direction_y != block_size:
                    direction_y = -block_size
                    direction_x = 0

                elif event.key == pygame.K_DOWN and direction_y != -block_size:
                    direction_y = block_size
                    direction_x = 0

        position_x += direction_x
        position_y += direction_y

        if position_x >= width or position_x < 0 or position_y >= height or position_y < 0: # If the last block is in the windows or not

            game_over = True

        else:

            display.fill((color_red, color_green, color_blue))
            pygame.draw.rect(display, RED, [apple_x, apple_y, block_size, block_size])

            snake_head = []
            snake_head.append(position_x)
            snake_head.append(position_y)
            snake_body.append(snake_head)

            if position_x == apple_x and position_y == apple_y:

                no_apple_in_screen = True
                apple_parameter = 0

            elif first_body and apple_parameter >= apple_tam:

                del snake_body[0]

            else:

                apple_parameter += 1
                first_body = True


            for snake_body_segment in snake_body[:-1]:

                if snake_body_segment == snake_head:

                        game_over = True

            making_snake(snake_body)
            pygame.display.update()  # Upload all the changes of the display

            clock.tick(difficult * 5) # Frames per second

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= 256 or change_red < limit_colors:

                change_red *= -1
                color_red += change_red

            if color_green >= 256 or color_green < limit_colors:

                change_green *= -1
                color_green += change_green

            if color_blue >= 256 or color_blue < limit_colors:

                change_blue *= -1
                color_blue += change_blue

    display.fill(WHITE)
    message_to_screen("You suck!", BLACK, width/2 - 30, height/2)
    pygame.display.update()
    time.sleep(5)

    pygame.quit()
    sys.exit()
    quit()

SnakeGame()
