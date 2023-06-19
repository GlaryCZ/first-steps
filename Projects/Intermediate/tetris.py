import pygame
import random
import sys

# initialize it
pygame.init()

# configurations
FPS = 60
window_height = 800
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

class Square(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, -20)
        self.cycle = 0

    def check_collision(self): # TODO
        pass 

    def update(self, move):
        if self.cycle == FPS:
            self.cycle = 0
            self.rect.move_ip(move*30, 30)
        else:
            self.rect.move_ip(move*30, 0)
        if move == 0:
            self.cycle += 1

def get_block(): # TODO
    pass
square = Square()

squares = pygame.sprite.Group()
squares.add(square)






while True:
    #####

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (97, 0), (97, 700), 5)
    pygame.draw.line(screen, (255, 255, 255), (402, 0), (402, 700), 5)
    pygame.draw.line(screen, (255, 255, 255), (95, 702), (404, 702), 5)
    squares.update(0)
    squares.draw(screen)
    

    for i in range(9):
        pygame.draw.line(screen, (255, 255, 255), (i*30+130, 0), (i*30+130, 700), 1)
    for i in range(24):
        pygame.draw.line(screen, (255, 255, 255), (100, i*30-20), (399, i*30-20), 1)
    #####
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                squares.update(1)
            elif event.key == pygame.K_LEFT:
                squares.update(-1)
        else:
            move = 0