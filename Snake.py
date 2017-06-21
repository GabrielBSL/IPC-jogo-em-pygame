import pygame, os, sys, random, time

pygame.init()

# ------------ sound configurations ------------ #

eating_apple = pygame.mixer.Sound("Sounds/apple.wav")
wrecking_intro = pygame.mixer.Sound("Sounds/glass.wav")
game_over_sound = pygame.mixer.Sound("Sounds/gameover.wav")
intro_sound = pygame.mixer.Sound("Sounds/intro_sound.wav")
load_error = pygame.mixer.Sound("Sounds/load_error.wav")

pygame.mixer.music.set_volume(1)

# ------------ sound configurations ------------ #

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

pygame.display.set_caption("Snake Game")
pygame.font.init()

normal_font = pygame.font.SysFont(None, 25)
pixeled_large_font = pygame.font.SysFont("Pixeled Regular", 80)
normal_large_font = pygame.font.SysFont(None, 50)
normal_big_font = pygame.font.SysFont(None, 80)

block_size = 10

snake_head_sprite = pygame.image.load("Images/snake_head.png")
apple_sprite = pygame.image.load("Images/apple.png")

clock = pygame.time.Clock()

# ------------ pattern general configurations ------------ #

def begin():

    display.fill(WHITE)
    message_to_screen("Jump Intro?", BLACK, 0, -200, True, 5)
    message_to_screen("Yes", BLACK, -100, 100, True, 5)
    message_to_screen("No", BLACK, 100, 100, True, 5)
    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                end()

        if 380 > mouse[0] > 320 and 420 > mouse[1] > 380:

            if click[0] and one_click:
                pygame.mixer.music.load("Sounds/menu.wav")
                pygame.mixer.music.play(-1)
                menu(0)
                one_click = False

            message_to_screen("Yes", (color_red, color_green, color_blue), -100, 100, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Yes", BLACK, -100, 100, True, 5)
            pygame.display.update()
            one_click = True

        if 570 > mouse[0] > 530 and 420 > mouse[1] > 380:

            if click[0] and one_click:
                intro1()
                one_click = False

            message_to_screen("No", (color_red, color_green, color_blue), 100, 100, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("No", BLACK, 100, 100, True, 5)
            pygame.display.update()
            one_click = True

# ------------ intros ------------ #

def intro1():
    display.fill(BLACK)

    limit_colors = 170

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    pygame.draw.rect(display, WHITE, [200, 250, 500, 100])
    for draw_rect in range (301):

        pygame.draw.rect(display, RED, [210, 260, draw_rect, 80])
        message_to_screen("Loading", (color_red, color_green, color_blue), 0, 80, True, 5)

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

        pygame.display.update()
        time.sleep(0.005)

    pygame.time.wait(700)
    pygame.mixer.Sound.play(load_error)
    pygame.time.wait(300)

    for intro_shake in range (44):

        shake_display = random.randrange(0, 150)
        display.fill(BLACK)

        color_red = random.randint(0, 255)
        color_blue = random.randint(0, 255)
        color_green = random.randint(0, 255)

        pygame.draw.rect(display, WHITE, [200 - shake_display, 250 - shake_display, 500, 100])
        pygame.draw.rect(display, RED, [210 - shake_display, 260 - shake_display, 300, 80])
        message_to_screen("Loading", (color_red, color_green, color_blue), 0 - shake_display, 80 - shake_display, True, 5)
        pygame.display.update()
        time.sleep(0.025)

        color_red = random.randint(0, 255)
        color_blue = random.randint(0, 255)
        color_green = random.randint(0, 255)

        shake_display = random.randrange(0, 150)
        display.fill(BLACK)
        pygame.draw.rect(display, WHITE, [200 - shake_display, 250 + shake_display, 500, 100])
        pygame.draw.rect(display, RED, [210 - shake_display, 260 + shake_display, 300, 80])
        message_to_screen("Loading", (color_red, color_green, color_blue), 0 - shake_display, 80 + shake_display, True, 5)
        pygame.display.update()
        time.sleep(0.025)

        color_red = random.randint(0, 255)
        color_blue = random.randint(0, 255)
        color_green = random.randint(0, 255)

        shake_display = random.randrange(0, 150)
        display.fill(BLACK)
        pygame.draw.rect(display, WHITE, [200 + shake_display, 250 - shake_display, 500, 100])
        pygame.draw.rect(display, RED, [210 + shake_display, 260 - shake_display, 300, 80])
        message_to_screen("Loading", (color_red, color_green, color_blue), 0 + shake_display, 80 - shake_display, True, 5)
        pygame.display.update()
        time.sleep(0.025)

        color_red = random.randint(0, 255)
        color_blue = random.randint(0, 255)
        color_green = random.randint(0, 255)

        shake_display = random.randrange(0, 150)
        display.fill(BLACK)
        pygame.draw.rect(display, WHITE, [200 + shake_display, 250 + shake_display, 500, 100])
        pygame.draw.rect(display, RED, [210 + shake_display, 260 + shake_display, 300, 80])
        message_to_screen("Loading", (color_red, color_green, color_blue), 0 + shake_display, 80 + shake_display, True, 5)
        pygame.display.update()
        time.sleep(0.025)

    display.fill(BLACK)
    pygame.draw.rect(display, WHITE, [200, 250, 500, 100])
    pygame.draw.rect(display, RED, [210, 260, 300, 80])
    message_to_screen("Loading", WHITE, 0, 80, True, 5)
    pygame.display.update()
    pygame.time.wait(1000)
    image_intro = pygame.image.load("Images/crash_load.png")

    fall_screen = 1
    while fall_screen <= 600:

        display.blit(image_intro, [0, 0])
        pygame.draw.rect(display, BLACK, [0, 0 + fall_screen, 900, 600])
        pygame.draw.rect(display, WHITE, [200, 250 + fall_screen, 500, 100])
        pygame.draw.rect(display, WHITE, [200, 250 + fall_screen, 500, 100])
        pygame.draw.rect(display, RED, [210, 260 + fall_screen, 300, 80])
        message_to_screen("Loading", WHITE, 0, 80 + fall_screen, True, 5)
        pygame.display.update()
        fall_screen += fall_screen
        time.sleep(0.025)

    pygame.mixer.Sound.play(wrecking_intro)

    display.blit(image_intro, [0, 0])
    pygame.display.update()
    pygame.time.wait(3000)

    fall_screen = 1
    while fall_screen <= 600:

        display.fill(BLACK)
        display.blit(image_intro, [0, fall_screen])
        pygame.display.update()
        fall_screen += fall_screen
        time.sleep(0.025)

    pygame.mixer.Sound.play(wrecking_intro)

    display.fill(BLACK)
    pygame.display.update()
    pygame.time.wait(4000)

    intro2()

def intro2():

    image_developer_1 = pygame.image.load('Images/developer_1.png')
    image_developer_2 = pygame.image.load('Images/developer_2.png')
    image_developer_3 = pygame.image.load('Images/developer_3.png')
    image_developer_4 = pygame.image.load('Images/developer_4.png')
    image_developer_5 = pygame.image.load('Images/developer_5.png')
    image_developer_head = pygame.image.load('Images/head_developer.png')

    for i in range (301):

        display.fill(BLACK)
        display.blit(image_developer_1, [350, i])
        pygame.display.update()

    for i in range(601):
        display.fill(BLACK)
        display.blit(image_developer_1, [350, 300])
        display.blit(image_developer_2, [i - 250, 330])
        pygame.display.update()

    for i in range(601):
        display.fill(BLACK)
        display.blit(image_developer_1, [350, 300])
        display.blit(image_developer_2, [350, 330])
        display.blit(image_developer_3, [950 - i, 360])
        pygame.display.update()

    for i in range(601):
        display.fill(BLACK)
        display.blit(image_developer_1, [350, 300])
        display.blit(image_developer_2, [350, 330])
        display.blit(image_developer_3, [350, 360])
        display.blit(image_developer_4, [i - 250, 390])
        pygame.display.update()

    for i in range(301):
        display.fill(BLACK)
        display.blit(image_developer_1, [350, 300])
        display.blit(image_developer_2, [350, 330])
        display.blit(image_developer_3, [350, 360])
        display.blit(image_developer_4, [350, 390])
        display.blit(image_developer_5, [350, 720 - i])
        pygame.display.update()

    pygame.mixer.Sound.play(intro_sound)

    for rotate in range (721):
        display.fill(BLACK)
        display.blit(image_developer_1, [350, 300])
        display.blit(image_developer_2, [350, 330])
        display.blit(image_developer_3, [350, 360])
        display.blit(image_developer_4, [350, 390])
        display.blit(image_developer_5, [350, 420])

        head_sprite = pygame.transform.rotate(image_developer_head, rotate)
        display.blit(head_sprite, [rotate - 400, 100])
        pygame.display.update()
        time.sleep(0.002)

    for max_shake in range (75):

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 + shake, 300 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 + shake, 330 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 + shake, 360 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 + shake, 390 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 + shake, 420 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 + shake, 100 + shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 - shake, 300 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 - shake, 330 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 - shake, 360 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 - shake, 390 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 - shake, 420 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 - shake, 100 + shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 + shake, 300 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 + shake, 330 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 + shake, 360 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 + shake, 390 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 + shake, 420 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 + shake, 100 - shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 - shake, 300 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 - shake, 330 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 - shake, 360 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 - shake, 390 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 - shake, 420 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 - shake, 100 - shake])
        pygame.display.update()
        time.sleep(0.002)

    max_shake = 75
    while max_shake > 0:
        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 + shake, 300 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 + shake, 330 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 + shake, 360 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 + shake, 390 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 + shake, 420 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 + shake, 100 + shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 - shake, 300 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 - shake, 330 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 - shake, 360 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 - shake, 390 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 - shake, 420 + shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 - shake, 100 + shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 + shake, 300 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 + shake, 330 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 + shake, 360 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 + shake, 390 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 + shake, 420 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 + shake, 100 - shake])
        pygame.display.update()
        time.sleep(0.002)

        display.fill(BLACK)
        shake = random.randint(0, max_shake)
        display.blit(image_developer_1, [350 - shake, 300 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_2, [350 - shake, 330 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_3, [350 - shake, 360 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_4, [350 - shake, 390 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_5, [350 - shake, 420 - shake])

        shake = random.randint(0, max_shake)
        display.blit(image_developer_head, [320 - shake, 100 - shake])
        pygame.display.update()
        time.sleep(0.002)

        max_shake -= 1

    time.sleep(3)

    intro3()

def intro3():

    uea_image = pygame.image.load('Images/UEA.jpg')
    est_image = pygame.image.load('Images/EST.png')
    pyg_image = pygame.image.load('Images/pygame.png')

    for transition in range (1500):

        display.fill(BLACK)
        display.blit(pyg_image, [transition - 600, 200])
        pygame.display.update()
        time.sleep(0.0001)

    for transition in range (1500):

        display.fill(BLACK)
        display.blit(uea_image, [900 - transition, 100])
        display.blit(est_image, [900 - transition, 350])
        pygame.display.update()
        time.sleep(0.0001)

    menu(1)

# ------------ intros ------------ #

def menu(opening):

    snake_icon = pygame.image.load('Images/snake_cute.png')
    snake_name = pygame.image.load('Images/snake_name.png')

    if opening:

        for blanking in range (256):

            display.fill((blanking, blanking, blanking))
            pygame.display.update()
            time.sleep(0.005)

        time.sleep(0.1)

        pygame.mixer.music.load("Sounds/menu.wav")
        pygame.mixer.music.play(-1)

        for transition in range(251):
            display.fill(WHITE)
            display.blit(snake_icon, [360, transition - 200])
            pygame.display.update()
            time.sleep(0.005)

        time.sleep(0.1)

        for transition in range(401):
            display.fill(WHITE)
            display.blit(snake_icon, [360, 50])
            display.blit(snake_name, [260, 600 - transition])
            pygame.display.update()
            time.sleep(0.0001)

            if transition == 310:

                pygame.mixer.Sound.play(eating_apple)

        time.sleep(1)

        for transition in range(201):
            display.fill(WHITE)
            display.blit(snake_icon, [360, 50])
            display.blit(snake_name, [260, 200])
            message_to_screen("Play", RED, 180, 600 - transition, False, 6)
            pygame.display.update()
            time.sleep(0.0001)

            if transition == 110:

                pygame.mixer.Sound.play(eating_apple)

        for transition in range(201):
            display.fill(WHITE)
            display.blit(snake_icon, [360, 50])
            display.blit(snake_name, [260, 200])
            message_to_screen("Play", RED, 180, 400, False, 6)
            message_to_screen("About", BLACK, 360, 600 - transition, False, 6)
            pygame.display.update()
            time.sleep(0.0001)

            if transition == 110:
                pygame.mixer.Sound.play(eating_apple)

        for transition in range(201):
            display.fill(WHITE)
            display.blit(snake_icon, [360, 50])
            display.blit(snake_name, [260, 200])
            message_to_screen("Play", RED, 180, 400, False, 6)
            message_to_screen("About", BLACK, 360, 400, False, 6)
            message_to_screen("Quit", BLACK, 600, 600 - transition, False, 6)
            pygame.display.update()
            time.sleep(0.0001)

            if transition == 110:
                pygame.mixer.Sound.play(eating_apple)

    display.fill(WHITE)
    display.blit(snake_icon, [360, 50])
    display.blit(snake_name, [260, 200])
    message_to_screen("Play", RED, 180, 400, False, 6)
    message_to_screen("About", BLACK, 360, 400, False, 6)
    message_to_screen("Quit", BLACK, 600, 400, False, 6)
    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 300 > mouse[0] > 180 and 460 > mouse[1] > 400:

            if click[0] and one_click:

                choose_mode()
                one_click = False

            message_to_screen("Play", (color_red, color_green, color_blue), 180, 400, False, 6)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Play", RED, 180, 400, False, 6)
            pygame.display.update()
            one_click = True

        if 530 > mouse[0] > 360 and 460 > mouse[1] > 400:

            if click[0] and one_click:

                about()
                one_click = False

            message_to_screen("About", (color_red, color_green, color_blue), 360, 400, False, 6)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:
            message_to_screen("About", BLACK, 360, 400, False, 6)
            pygame.display.update()
            one_click = True

        if 720 > mouse[0] > 600 and 460 > mouse[1] > 400:

            if click[0] and one_click:

                quit()
                one_click = False

            message_to_screen("Quit", (color_red, color_green, color_blue), 600, 400, False, 6)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:
            message_to_screen("Quit", BLACK, 600, 400, False, 6)
            pygame.display.update()
            one_click = True

def choose_mode():

    display.fill(WHITE)
    message_to_screen("Choose mode", BLACK, 0, -200, True, 5)
    message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
    message_to_screen("Normal mode", BLACK, -300, 0, True, 5)
    message_to_screen("Psychedelic mode", BLACK, -7, 0, True, 5)
    message_to_screen("Invisible mode", BLACK, 300, 0, True, 5)
    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 570 > mouse[0] > 330 and 520 > mouse[1] > 480:

            if click[0] and one_click:

                menu(0)
                one_click = False

            message_to_screen("Back to menu", (color_red, color_green, color_blue), 0, 200, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
            pygame.display.update()
            one_click = True

        if 275 > mouse[0] > 35 and 320 > mouse[1] > 280:

            if click[0] and one_click:

                choose_difficulty(1)
                one_click = False

            message_to_screen("Normal mode", (color_red, color_green, color_blue), -300, 0, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Normal mode", BLACK, -300, 0, True, 5)
            pygame.display.update()
            one_click = True

        if 600 > mouse[0] > 290 and 320 > mouse[1] > 280:

            if click[0] and one_click:
                choose_difficulty(2)
                one_click = False

            message_to_screen("Psychodelic mode", (color_red, color_green, color_blue), -7, 0, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:
            message_to_screen("Psychodelic mode", BLACK, -7, 0, True, 5)
            pygame.display.update()
            one_click = True

        if 880 > mouse[0] > 630 and 320 > mouse[1] > 280:

            if click[0] and one_click:
                choose_difficulty(3)
                one_click = False

            message_to_screen("Invisible mode", (color_red, color_green, color_blue), 300, 0, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:
            message_to_screen("Invisible mode", BLACK, 300, 0, True, 5)
            pygame.display.update()
            one_click = True

def choose_difficulty(mode):

    display.fill(WHITE)
    message_to_screen("Choose difficulty", BLACK, 0, -200, True, 5)
    message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
    message_to_screen("1", BLACK, -320, -50, True, 5)
    message_to_screen("2", BLACK, -160, -50, True, 5)
    message_to_screen("3", BLACK, 0, -50, True, 5)
    message_to_screen("4", BLACK, 160, -50, True, 5)
    message_to_screen("5", BLACK, 320, -50, True, 5)
    message_to_screen("6", BLACK, -320, 50, True, 5)
    message_to_screen("7", BLACK, -160, 50, True, 5)
    message_to_screen("8", BLACK, 0, 50, True, 5)
    message_to_screen("9", BLACK, 160, 50, True, 5)
    message_to_screen("10", BLACK, 320, 50, True, 5)
    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 570 > mouse[0] > 330 and 520 > mouse[1] > 480:

            if click[0] and one_click:
                choose_mode()
                one_click = False

            message_to_screen("Back to menu", (color_red, color_green, color_blue), 0, 200, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
            pygame.display.update()
            one_click = True

        if 140 > mouse[0] > 120 and 270 > mouse[1] > 230:

            if click[0] and one_click:
                choose_wall(mode, 1)
                one_click = False

            message_to_screen("1", (color_red, color_green, color_blue), -320, -50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("1", BLACK, -320, -50, True, 5)
            pygame.display.update()
            one_click = True

        if 300 > mouse[0] > 280 and 270 > mouse[1] > 230:

            if click[0] and one_click:
                choose_wall(mode, 2)
                one_click = False

            message_to_screen("2", (color_red, color_green, color_blue), -160, -50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("2", BLACK, -160, -50, True, 5)
            pygame.display.update()
            one_click = True

        if 460 > mouse[0] > 440 and 270 > mouse[1] > 230:

            if click[0] and one_click:
                choose_wall(mode, 3)
                one_click = False

            message_to_screen("3", (color_red, color_green, color_blue), 0, -50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("3", BLACK, 0, -50, True, 5)
            pygame.display.update()
            one_click = True

        if 620 > mouse[0] > 600 and 270 > mouse[1] > 230:

            if click[0] and one_click:
                choose_wall(mode, 4)
                one_click = False

            message_to_screen("4", (color_red, color_green, color_blue), 160, -50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("4", BLACK, 160, -50, True, 5)
            pygame.display.update()
            one_click = True

        if 780 > mouse[0] > 760 and 270 > mouse[1] > 230:

            if click[0] and one_click:
                choose_wall(mode, 5)
                one_click = False

            message_to_screen("5", (color_red, color_green, color_blue), 320, -50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("5", BLACK, 320, -50, True, 5)
            pygame.display.update()
            one_click = True

        if 140 > mouse[0] > 120 and 370 > mouse[1] > 330:

            if click[0] and one_click:
                choose_wall(mode, 6)
                one_click = False

            message_to_screen("6", (color_red, color_green, color_blue), -320, 50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("6", BLACK, -320, 50, True, 5)
            pygame.display.update()
            one_click = True

        if 300 > mouse[0] > 280 and 370 > mouse[1] > 330:

            if click[0] and one_click:
                choose_wall(mode, 7)
                one_click = False

            message_to_screen("7", (color_red, color_green, color_blue), -160, 50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("7", BLACK, -160, 50, True, 5)
            pygame.display.update()
            one_click = True

        if 460 > mouse[0] > 440 and 370 > mouse[1] > 330:

            if click[0] and one_click:
                choose_wall(mode, 8)
                one_click = False

            message_to_screen("8", (color_red, color_green, color_blue), 0, 50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("8", BLACK, 0, 50, True, 5)
            pygame.display.update()
            one_click = True

        if 620 > mouse[0] > 600 and 370 > mouse[1] > 330:

            if click[0] and one_click:
                choose_wall(mode, 9)
                one_click = False

            message_to_screen("9", (color_red, color_green, color_blue), 160, 50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("9", BLACK, 160, 50, True, 5)
            pygame.display.update()
            one_click = True

        if 790 > mouse[0] > 750 and 370 > mouse[1] > 330:

            if click[0] and one_click:
                choose_wall(mode, 10)
                one_click = False

            message_to_screen("10", (color_red, color_green, color_blue), 320, 50, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("10", BLACK, 320, 50, True, 5)
            pygame.display.update()
            one_click = True

def choose_wall(mode, difficulty):

    display.fill(WHITE)
    message_to_screen("Choose style", BLACK, 0, -200, True, 5)
    message_to_screen("with wall in edges", BLACK, 210, 0, True, 5)
    message_to_screen("without wall in edges", BLACK, -200, 0, True, 5)
    message_to_screen("Back to menu", BLACK, 0, 200, True, 5)

    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 570 > mouse[0] > 330 and 520 > mouse[1] > 480:

            if click[0] and one_click:
                choose_difficulty()
                one_click = False

            message_to_screen("Back to menu", (color_red, color_green, color_blue), 0, 200, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
            pygame.display.update()
            one_click = True

        if 810 > mouse[0] > 510 and 320 > mouse[1] > 280:

            if click[0] and one_click:
                SnakeGame(mode, difficulty, 1)
                one_click = False

            message_to_screen("with wall in edges", (color_red, color_green, color_blue), 210, 0, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("with wall in edges", BLACK, 210, 0, True, 5)
            pygame.display.update()
            one_click = True

        if 430 > mouse[0] > 70 and 320 > mouse[1] > 280:

            if click[0] and one_click:
                SnakeGame(mode, difficulty, 2)
                one_click = False

            message_to_screen("without wall in edges", (color_red, color_green, color_blue), -200, 0, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("without wall in edges", BLACK, -200, 0, True, 5)
            pygame.display.update()
            one_click = True

def SnakeGame(mode, difficulty, wall):

    # ------------ pattern game configurations ------------ #

    pygame.mixer.music.load("Sounds/game_sound.wav")
    pygame.mixer.music.play(-1)

    position_x = width / 2
    position_y = height / 2
    direction_x = 0
    direction_y = 0

    points = 0

    limit_colors = 170

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    no_apple_in_screen = True

    difficult = difficulty
    game_over = False

    if mode != 1:

        limit_colors = 170

        color_red = limit_colors
        color_green = limit_colors
        color_blue = limit_colors

        change_red = 1
        change_green = 2
        change_blue = 4

        background_color = (color_red, color_green, color_blue)

    else:

        background_color = WHITE

    direction_head = 0

    first_body = False
    apple_tam = 3
    apple_parameter = 3

    snake_body = []

    # ------------ pattern game configurations ------------ #

    while True:

        no_auto_crash = True

        display.fill(background_color)
        message_to_screen("'space' to pause", BLACK, 760, 10, False, 1)

        while no_apple_in_screen:

            apple_x = random.randrange(0, width / block_size) * block_size
            apple_y = random.randrange(0, height / block_size) * block_size
            apple_location = [apple_x, apple_y]

            blank_position = True

            for snake_body_lenght in snake_body:

                if snake_body_lenght == apple_location:

                    blank_position = False

            if blank_position:

                no_apple_in_screen = False

        while game_over:

            display.fill(WHITE)
            message_to_screen("Game Over", RED, 0, -90, True, 4)
            message_to_screen("press P to play again or Q to back to menu", BLACK, 0, 50, True, 5)

            score(points, 390, 400, 2)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    end()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q or event.type == pygame.QUIT:

                        pygame.mixer.music.load("Sounds/menu.wav")
                        pygame.mixer.music.play(-1)
                        menu(0)

                    elif event.key == pygame.K_p:

                        SnakeGame(mode, difficulty, wall)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

            if event.type == pygame.KEYDOWN:

                if position_x >= 0 and position_x < width and position_y >= 0 and position_y < height:

                    if event.key == pygame.K_LEFT and direction_x != block_size and no_auto_crash:
                        direction_x = -block_size
                        direction_y = 0
                        direction_head = 2
                        no_auto_crash = False

                    elif event.key == pygame.K_RIGHT and direction_x != -block_size and no_auto_crash:
                        direction_x = block_size
                        direction_y = 0
                        direction_head = 0
                        no_auto_crash = False

                    elif event.key == pygame.K_UP and direction_y != block_size and no_auto_crash:
                        direction_y = -block_size
                        direction_x = 0
                        direction_head = 1
                        no_auto_crash = False

                    elif event.key == pygame.K_DOWN and direction_y != -block_size and no_auto_crash:
                        direction_y = block_size
                        direction_x = 0
                        direction_head = 3
                        no_auto_crash = False

                    elif event.key == pygame.K_SPACE:

                        pause()

        position_x += direction_x
        position_y += direction_y

        if (position_x >= width or position_x < 0 or position_y >= height or position_y < 0): # If the last block is in the windows or not

            if wall == 1:
                game_over = True
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(game_over_sound)

            else:

                if position_x >= width:
                    position_x = -block_size

                elif position_x < 0:
                    position_x = width

                elif position_y >= height:
                    position_y = -block_size

                else:
                    position_y = height

        else:

            score(points, 10, 10, 1)

            pygame.draw.rect(display, background_color, [apple_x, apple_y, block_size, block_size])
            display.blit(apple_sprite, [apple_x, apple_y])

            snake_head = []
            snake_head.append(position_x)
            snake_head.append(position_y)
            snake_body.append(snake_head)

            if position_x == apple_x and position_y == apple_y:

                points += 10
                pygame.mixer.Sound.play(eating_apple)
                no_apple_in_screen = True
                apple_parameter = 0

            elif first_body and apple_parameter >= apple_tam:

                del snake_body[0]

            else:

                apple_parameter += 1
                first_body = True

            for snake_body_segment in snake_body[:-1]:

                if (snake_body_segment == snake_head):

                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(game_over_sound)
                    game_over = True

            making_snake(snake_body, background_color, mode)

            if mode != 3:

                head_sprite = pygame.transform.rotate(snake_head_sprite, direction_head * 90)
                display.blit(head_sprite, [position_x, position_y])

            pygame.display.update()  # Upload all the changes of the display

            clock.tick(difficult * 5) # Frames per second

            if mode != 1:

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

                background_color = (color_red, color_green, color_blue)

def score(points, pos_x, pos_y, type):

    if type == 1:
        text = normal_font.render("Score: " + str(points), True, BLACK)

    if type == 2:
        text = normal_large_font.render("Score: " + str(points), True, BLACK)

    display.blit(text, [pos_x, pos_y])
    pygame.display.update()

def pause():

    pygame.mixer.music.pause()
    pause = True
    display.fill(WHITE)
    message_to_screen("Paused", BLACK, 0, -100, True, 6)
    message_to_screen("Press 'p' to unpause", BLACK, 0, 100, True, 5)
    message_to_screen("Press 'q' to go to menu", BLACK, 0, 150, True, 5)
    pygame.display.update()

    while pause:

        for event in pygame.event.get():

            if event.key == pygame.K_p:
                pause = False
                pygame.mixer.music.unpause()

            if event.key == pygame.K_q:
                pygame.mixer.music.load("Sounds/menu.wav")
                pygame.mixer.music.play(-1)
                menu(0)

            if event.type == pygame.QUIT:

                end()

def making_snake(snakelist, background_color, mode):

    for pos_x_y in snakelist[:-1]:

        if mode != 3:

            pygame.draw.rect(display, GREEN, [pos_x_y[0], pos_x_y[1], block_size, block_size])# Create a block with the two firsts parameters being the position and the others two being the size

        else:

            pygame.draw.rect(display, (background_color[0] - 5, background_color[1] - 5, background_color[2] - 5), [pos_x_y[0], pos_x_y[1], block_size, block_size])

    pos_x_y = snakelist[-1]

    if mode != 3:

        pygame.draw.rect(display, background_color, [pos_x_y[0], pos_x_y[1], block_size, block_size])

    else:

        pygame.draw.rect(display, (background_color[0] - 5, background_color[1] - 5, background_color[2] - 5), [pos_x_y[0], pos_x_y[1], block_size, block_size])

def text_objects(text, color, type):

    if type == 1:
        text_surface = normal_font.render(text, True, color)

    elif type == 4:
        text_surface = pixeled_large_font.render(text, True, color)

    elif type == 5:
        text_surface = normal_large_font.render(text, True, color)

    else:
        text_surface = normal_big_font.render(text, True, color)

    return text_surface, text_surface.get_rect()

def message_to_screen (message, color, pos_x, pos_y, centerized, type):

    if centerized:
        text_surface, text_rect = text_objects(message, color, type)
        text_rect.center = (width / 2) + pos_x, (height / 2) + pos_y
        display.blit(text_surface, text_rect)

    else:
        if type == 1:
            screen_text = normal_font.render(message, True, color)

        elif type == 2:
            screen_text = pixeled_small_font.render(message, True, color)

        elif type == 3:
            screen_text = pixeled_medium_font.render(message, True, color)

        elif type == 4:
            screen_text = pixeled_large_font.render(message, True, color)

        elif type == 5:
            screen_text = normal_large_font.render(message, True, color)

        else:
            screen_text = normal_big_font.render(message, True, color)

        display.blit(screen_text, [pos_x, pos_y])

def about():

    display.fill(WHITE)
    message_to_screen("Developers:", BLACK, 30, 30, False, 6)
    message_to_screen("Gabriel Barroso", BLACK, 50, 120, False, 5)
    message_to_screen("Hugo Thadeu", BLACK, 50, 170, False, 5)
    message_to_screen("Victor Summer", BLACK, 50, 220, False, 5)
    message_to_screen("Frederico", BLACK, 50, 270, False, 5)
    message_to_screen("Guilherme", BLACK, 50, 320, False, 5)
    message_to_screen("Instructor: Dr. Jucimar Jr", BLACK, 20, 400, False, 5)

    squad_developers_1 = pygame.image.load('Images/crash_load_minimized.png')
    squad_developers_2 = pygame.image.load('Images/developer_minimized.png')
    uea_min = pygame.image.load('Images/UEA.jpg')
    est_min = pygame.image.load('Images/EST.png')

    display.blit(squad_developers_1, [350, 20])
    display.blit(squad_developers_2, [350, 240])
    display.blit(uea_min, [630, 0])
    display.blit(est_min, [630, 200])

    message_to_screen("All rights reserved", BLACK, 80, 450, False, 1)

    message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    pygame.display.update()

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 570 > mouse[0] > 330 and 520 > mouse[1] > 480:

            if click[0] and one_click:
                choose_mode()
                one_click = False

            message_to_screen("Back to menu", (color_red, color_green, color_blue), 0, 200, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Back to menu", BLACK, 0, 200, True, 5)
            pygame.display.update()
            one_click = True

def quit():

    pygame.mixer.music.stop()
    display.fill(WHITE)
    message_to_screen("Are you Sure?", BLACK, 0, -200, True, 5)
    message_to_screen("Yes", BLACK, -100, 100, True, 5)
    message_to_screen("No", BLACK, 100, 100, True, 5)
    pygame.display.update()

    limit_colors = 170
    one_click = True

    color_red = limit_colors
    color_green = limit_colors
    color_blue = limit_colors

    change_red = 1
    change_green = 2
    change_blue = 4

    while True:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                end()

        if 380 > mouse[0] > 320 and 420 > mouse[1] > 380:

            if click[0] and one_click:

                end()
                one_click = False

            message_to_screen("Yes", (color_red, color_green, color_blue), -100, 100, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("Yes", BLACK, -100, 100, True, 5)
            pygame.display.update()
            one_click = True

        if 570 > mouse[0] > 530 and 420 > mouse[1] > 380:

            if click[0] and one_click:

                pygame.mixer.music.load("Sounds/menu.wav")
                pygame.mixer.music.play(-1)
                menu(0)
                one_click = False

            message_to_screen("No", (color_red, color_green, color_blue), 100, 100, True, 5)
            pygame.display.update()

            color_red += change_red
            color_green += change_green
            color_blue += change_blue

            if color_red >= limit_colors or change_red < 0:
                change_red *= -1
                color_red += change_red

            if color_green >= limit_colors or color_green < 0:
                change_green *= -1
                color_green += change_green

            if color_blue >= limit_colors or color_blue < 0:
                change_blue *= -1
                color_blue += change_blue

        else:

            message_to_screen("No", BLACK, 100, 100, True, 5)
            pygame.display.update()
            one_click = True

def end():

    pygame.mixer.music.stop()
    display.fill(WHITE)
    message_to_screen("Thanks for Playing!", BLACK, 0, 0, True, 6)
    pygame.display.update()
    time.sleep(5)

    pygame.quit()
    quit()
    sys.exit()

begin()
