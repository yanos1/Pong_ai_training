import random

WHITE = (255, 255, 255)

BALL_SIZE = 15


class Ball:
    COLOR = WHITE
    SIZE = BALL_SIZE
    MAX_SPEED = 5

    def __init__(self, x, y):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.x_speed = random.choice([-1, 1]) * self.MAX_SPEED
        self.y_speed = random.choice([-2.3, 2.3])

    def draw_ball(self, window, ball_image):
        window.blit(ball_image, (self.x, self.y))

    def move_ball(self):
        self.x += self.x_speed
        self.y += self.y_speed
