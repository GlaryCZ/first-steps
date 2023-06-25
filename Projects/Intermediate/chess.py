import pygame
import random
import sys

# initialize it
pygame.init()

# configurations
FPS = 30
window_height = 800
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Šachy pičo')
clock = pygame.time.Clock()

turn = "w" # "w" / "b"
FIGURKA = None

white_figurky = {"p1": [0, 1, True], "p2": [1, 1, True], "p3": [2, 1, True], "p4": [3, 1, True], "p5": [4, 1, True], "p6": [5, 1, True], "p7": [6, 1, True], "p8": [7, 1, True]}

black_figurky = {}

def draw_figurku(x, y):
    pygame.draw.rect(screen, (255, 2, 0),pygame.Rect(x*100+30, y*100+30, 20, 20))

def draw_figurky(figurky):
    for i in range(8):
        fig = "p"+str(i+1)
        pos = figurky[fig]
        if fig != FIGURKA:
            draw_figurku(pos[0], pos[1])

def move_figurku(figurka, turn, pos):
    if turn == "w":
        if figurka[0] == "p" and pos == [white_figurky[figurka][0], white_figurky[figurka][1]+1]:
            white_figurky[figurka] = [white_figurky[figurka][0], white_figurky[figurka][1]+1, False]
        elif figurka[0] == "p" and pos == [white_figurky[figurka][0], white_figurky[figurka][1]+2] and white_figurky[figurka][2]:
            white_figurky[figurka] = [white_figurky[figurka][0], white_figurky[figurka][1]+2, False]
    else:
        figurky = black_figurky

def get_figurka(x, y, turn):
    if turn == "w":
        for key, value in white_figurky.items():
            if value[:-1] == [x, y]:
                return key

def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    x = x // 100
    y = y // 100
    return x, y

def draw_board():
    screen.fill((30, 30, 30))
    for x in range(8):
        for y in range(8):
            if (x+y) % 2 == 0:

                pygame.draw.rect(screen, (200, 200, 200),pygame.Rect(x*100, y*100, 100, 100))

def create_figurky():
    pass


while True:
    draw_board()
    draw_figurky(white_figurky)
    if FIGURKA != None:
        screen.blit(pygame.Surface((30, 30)), pygame.mouse.get_pos()) # TODO kurzor figurka

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_figurku("p1", turn, [0, white_figurky["p1"][1]+1])
            if event.key == pygame.K_LEFT:
                move_figurku("p1", turn, [0, white_figurky["p1"][1]+2])
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = get_mouse_pos()
            if turn == "w":
                FIGURKA = get_figurka(x, y, turn)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = get_mouse_pos()
            if FIGURKA != None:
                move_figurku(FIGURKA, turn, [x, y])
                FIGURKA = None