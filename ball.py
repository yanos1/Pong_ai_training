import pygame
import random
WHITE = (255,255,255)

BALL_SIZE = 8


class Ball:
    COLOR = WHITE
    SIZE = BALL_SIZE
    MAX_SPEED = 10

    def __init__(self, x, y):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.x_speed = random.choice([-1,1]) * self.MAX_SPEED
        self.y_speed = random.uniform(-3.5,3.5)

    def draw_ball(self,window,ball_image):
        window.blit(ball_image,(self.x,self.y))

    def move_ball(self):
        self.x += self.x_speed
        self.y += self.y_speed



