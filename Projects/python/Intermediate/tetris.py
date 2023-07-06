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
pygame.display.set_caption('Tetris pičo')
clock = pygame.time.Clock()

checked_collision = False
s = False

collision_blocks = [(100, 700), (130, 700), (160, 700), (190, 700), (220, 700), (250, 700), (280, 700), (310, 700), (340, 700), (370, 700)]

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*30+100, y*30-20)
        self.cycle = 0

    def check_collision(self): # TODO
        global squares, checked_collision
        if (self.rect.topleft[0], self.rect.topleft[1]) in collision_blocks: 
            if not checked_collision:
                for sqr in squares:
                    collision_blocks.append((sqr.rect.topleft[0], sqr.rect.topleft[1]-30))
                    sqr.kill()
            self.kill()
            if len(squares) == 0:
                squares = get_block()
            checked_collision = True



    def update(self, move):
        global s
        i = 0
        if move == 0:
            self.cycle += 1
        elif move == 69:
            self.check_collision()
        if self.cycle == 10 and move == 0:
            self.cycle = 0
            self.rect.move_ip(0, 30)
            global checked_collision
            checked_collision = False
        elif move == -1:
            for sqrt in squares:
                if not (sqrt.rect.topleft[0]-30, sqrt.rect.topleft[1]) in collision_blocks and  sqrt.rect.topleft[0] != 100:
                    i += 1
            if i == 4 and not s:
                s = True
                for sqr in squares:
                    sqr.rect.move_ip(-30, 0)
        elif move == 1: # and self.rect[0] != 370 and not (self.rect.topleft[0]+30, self.rect.topleft[1]) in collision_blocks:
            for sqrt in squares:
                print(sqrt.rect.topleft[0])
                if not (sqrt.rect.topleft[0]+30, sqrt.rect.topleft[1]) in collision_blocks and  sqrt.rect.topleft[0] != 370:
                    i += 1
            if i == 4 and not s:
                s = True
                for sqr in squares:
                    sqr.rect.move_ip(30, 0)


def get_block(): # TODO
    global squares
    choice = random.randint(0, 6)
    print("get_block")
    print(collision_blocks)
    for sqr in squares:
        sqr.kill()
    if choice == 0:
        square1 = Square(1, 0)
        square2 = Square(1, 1)
        square3 = Square(2, 1)
        square4 = Square(2, 0)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)
    elif choice == 1:
        square1 = Square(1, 0)
        square2 = Square(1, 1)
        square3 = Square(1, 2)
        square4 = Square(2, 2)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)

    elif choice == 2:
        square1 = Square(1, 0)
        square2 = Square(1, 1)
        square3 = Square(1, 2)
        square4 = Square(1, 3)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)

    elif choice == 3:
        square1 = Square(1, 0)
        square2 = Square(2, 0)
        square3 = Square(3, 0)
        square4 = Square(2, -1)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)
    elif choice == 4:
        square1 = Square(1, 0)
        square2 = Square(1, 1)
        square3 = Square(1, 2)
        square4 = Square(0, 2)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)
    elif choice == 5: ######
        square1 = Square(1, 0)
        square2 = Square(2, 0)
        square3 = Square(2, 1)
        square4 = Square(3, 1)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)
    elif choice == 6:
        square1 = Square(3, 0)
        square2 = Square(2, 0)
        square3 = Square(2, 1)
        square4 = Square(1, 1)

        for sqr in [square1, square2, square3, square4]:
            squares.add(sqr)
        
    return squares
    


squares = pygame.sprite.Group()
squares = get_block()








while True:
    #####

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (97, 0), (97, 700), 5)
    pygame.draw.line(screen, (255, 255, 255), (402, 0), (402, 700), 5)
    pygame.draw.line(screen, (255, 255, 255), (95, 702), (404, 702), 5)
    squares.update(69)
    squares.update(0)
    s = False
    squares.draw(screen)
    print(squares)
    for i in range(len(collision_blocks)-10):
        pygame.draw.rect(screen,"red",(collision_blocks[i+10][0],collision_blocks[i+10][1],30,30))

    

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