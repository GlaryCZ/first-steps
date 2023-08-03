import pygame
import random
import sys
import neat
import os

# initialize it  vgv
pygame.init()

# configurations
frames_per_second = 60
window_height = 600
window_width = 800 

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('PONG AI')
clock = pygame.time.Clock()

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, "config.txt")
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

class Ball():
    def __init__(self, start_pos):
        self.pos = start_pos
        self.direction = [9, -1]
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos[0]-10, self.pos[1]-10, 20, 20))
    def update(self):
        self.pos = [self.pos[0]+self.direction[0], self.pos[1]+self.direction[1]]
        self.draw()
    def check_border_collision(self):
        if ball.pos[1] < 2 or ball.pos[1] > window_height-2:
            ball.direction[1] = -ball.direction[1]
    def check_table_collision(self):
        global ball
        if self.pos[0] < 5:
            # if self.pos[1] > table1.pos[1]-70 and self.pos[1] < table1.pos[1]+70:
            self.pong()
            # else: # bod pro ai
                # ball = Ball([400, 300])
        elif self.pos[0] > window_width-5:
            if self.pos[1] > table_ai.pos[1]-70 and self.pos[1] < table_ai.pos[1]+70:
                self.pong()
            else: # bod pro hrace
                ball = Ball([400, 300])
    def check_collisions(self):
        self.check_border_collision()
        self.check_table_collision()
    def pong(self):
        x_speed = random.randint(3, 10)
        y_speed = (10 - x_speed) * (random.choice([1, -1]))
        if self.pos[0] < 5:
            self.pos[0] = 5
            self.direction = [x_speed, y_speed]
        else:
            self.pos[0] = window_width-5
            self.direction = [-x_speed, y_speed]

class Table():
    def __init__(self, start_pos):
        self.pos = start_pos
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.pos[0]-5, self.pos[1]-60, 10, 120))

def draw_borders():
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, window_width, 3))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, window_height-3, window_width, 3))

def run_neat(config):
    p = neat.Population(config)
    # p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-27")
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1)) # ulozi kazdou "1" generaci

    winner = p.run(eval_genomes, 50)



ball = Ball([400, 300])
table1 = Table([0, window_height/2])
table_ai = Table([window_width, window_height/2])

def eval_genomes(genomes, config):
    for (genome_id, genome) in genomes:
        genome.fitness = 0
        while True:
            
            screen.fill((0, 0, 0))

            draw_borders()
            ball.check_collisions()
            ball.update()
            table1.draw()
            table_ai.draw()

            pygame.display.flip()
            clock.tick(frames_per_second)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if table1.pos[1] > 60:
                    table1.pos[1] -= 5
            if keys[pygame.K_DOWN]:
                if table1.pos[1] < window_height-60:
                    table1.pos[1] += 5


while True:
    
    screen.fill((0, 0, 0))

    draw_borders()
    ball.check_collisions()
    ball.update()
    table1.draw()
    table_ai.draw()

    pygame.display.flip()
    clock.tick(frames_per_second)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if table1.pos[1] > 60:
            table1.pos[1] -= 5
    if keys[pygame.K_DOWN]:
        if table1.pos[1] < window_height-60:
            table1.pos[1] += 5