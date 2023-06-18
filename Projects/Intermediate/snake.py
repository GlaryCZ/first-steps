import pygame
import random
import sys

# initialize it
pygame.init()

# configurations
frames_per_second = 10
window_height = 600
window_width = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Silly snake')
clock = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.pos = [(0, 0), (1, 0), (2, 0)]
        self.direction = 1
        self.eaten_apple = False

    def move(self, apple):
        if self.direction == 1: # right
            new_pos = (self.pos[-1][0]+1, self.pos[-1][1])
        elif self.direction == 2: # down
            new_pos = (self.pos[-1][0], self.pos[-1][1]+1)
        elif self.direction == 3: # left
            new_pos = (self.pos[-1][0]-1, self.pos[-1][1])
        elif self.direction == 4: # up
            new_pos = (self.pos[-1][0], self.pos[-1][1]-1)
        new_pos = (new_pos[0] % 30, new_pos[1] % 30)
        self.pos.append(new_pos)
        snake.check_apple(apple)
        if not self.eaten_apple:
            self.pos.pop(0)
        else:
            self.eaten_apple = False

    def draw(self):
        for pos in self.pos:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0]*20+1, pos[1]*20+1, 19, 19))

    def check_apple(self, apple):
        if self.pos[-1] == apple.pos:
            self.eaten_apple = True
            apple.pos = (random.randint(0, 29), random.randint(0, 29))

    def check_collision(self):
        if len(self.pos) != len(set(self.pos)):
            print("\n")
            print("You lost!")
            print("Your score was: {}".format(len(self.pos)))
            snake.__init__()
            apple.__init__()
            


class Apple():
    def __init__(self):
        self.pos = (5, 5)
    def draw(self):
       pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.pos[0]*20+1, self.pos[1]*20+1, 19, 19))


snake = Snake()
apple = Apple()

# forever loop
while True:
    # frame clock ticking
    
    screen.fill((0, 0, 0))
    
    snake.move(apple)
    snake.check_collision()
    apple.draw()
    snake.draw()

    pygame.display.flip()
    clock.tick(frames_per_second)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = 1
            if event.key == pygame.K_DOWN:
                snake.direction = 2 
            if event.key == pygame.K_LEFT:
                snake.direction = 3
            if event.key == pygame.K_UP:
                snake.direction = 4
    
        