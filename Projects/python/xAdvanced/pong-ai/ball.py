import pygame

# configurations
frames_per_second = 60
window_height = 600
window_width = 800 

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