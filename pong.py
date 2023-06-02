import pygame
import random
from display import Display
from ball import Ball
from pedals import Paddle


pygame.init()

# game assets #
pygame.display.set_caption('Pong')
PADDLE_IMAGE = pygame.image.load("paddle_improved.png")
BG_IMAGE = pygame.image.load("space_background.png")
BALL_IMAGE = pygame.image.load("Moon.png")

#  game settings ##
WIDTH = 830
HEIGHT = 550
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))
BALL_SIZE = 8
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 12
right_paddle_x = 15
right_paddle_y = (HEIGHT / 2) - PADDLE_HEIGHT / 2
left_paddle_x = WIDTH - 15 - PADDLE_WIDTH
left_paddle_y = (HEIGHT / 2) - PADDLE_HEIGHT / 2
petal_2_pos = (HEIGHT / 2) - PADDLE_HEIGHT / 2
BACKGROUND_COLOR = (0, 100, 140)
Y_AXIS_CHANGE = 0.09
MAX_POINTS = 10
########################


class GameInformation:
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score


class Game:
    def __init__(self):
        self.display = Display(WIDTH, HEIGHT, BACKGROUND_COLOR)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2)
        self.left_paddle = Paddle(right_paddle_x, right_paddle_y, PADDLE_WIDTH,
                                  PADDLE_HEIGHT)
        self.right_paddle = Paddle(left_paddle_x, left_paddle_y, PADDLE_WIDTH,
                                   PADDLE_HEIGHT)
        self.right_score = 0
        self.right_hits = 0
        self.left_score = 0
        self.left_hits = 0
        self.game_over = False

    def draw_all(self):
        self.display.draw_screen(self.display.screen, BG)
        self.display.draw_score(self.display.screen, self.left_score,
                                self.right_score)
        self.display.draw_hits(self.display.screen,self.left_hits,self.right_hits)
        self.ball.draw_ball(self.display.screen, BALL_IMAGE)
        self.right_paddle.draw_paddle(self.display.screen, PADDLE_IMAGE)
        self.left_paddle.draw_paddle(self.display.screen, PADDLE_IMAGE)
        if self.game_over:
            self.end_game()
        pygame.display.update()

    # def paddle_movement(self):
    #     keys = pygame.key.get_pressed()
    #
    #     if len(keys) > 0:
    #         if keys[pygame.K_UP] and self.right_paddle.y - self.right_paddle.SPEED > 0:
    #             self.right_paddle.move()
    #             return True
    #         if keys[pygame.K_DOWN] and self.right_paddle.y + self.right_paddle.height + self.right_paddle.SPEED < HEIGHT:
    #             self.right_paddle.move(up=False)
    #             return True
    #         if keys[pygame.K_w] and self.left_paddle.y - self.left_paddle.SPEED > 0:
    #             self.left_paddle.move()
    #             return True
    #         if keys[pygame.K_s] and self.left_paddle.y + self.left_paddle.height + self.left_paddle.SPEED < HEIGHT:
    #             self.left_paddle.move(up=False)
    #             return True
    #         return False

    def move_paddle(self, left=True, up=True):
        """
        Move the left or right paddle.
        :returns: boolean indicating if paddle movement is valid.
                  Movement is invalid if it causes paddle to go
                  off the screen
        """
        if left:
            if up and self.left_paddle.y - Paddle.SPEED < 0:
                return False
            if not up and self.left_paddle.y + PADDLE_HEIGHT > self.display.height:
                return False
            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - Paddle.SPEED < 0:
                return False
            if not up and self.right_paddle.y + PADDLE_HEIGHT > self.display.height:
                return False
            self.right_paddle.move(up)

        return True

    def ball_peddle_collision(self):
        if self.right_paddle.x <= self.ball.x + (
                BALL_SIZE // 2) <= self.right_paddle.x + PADDLE_WIDTH:
            if self.right_paddle.y <= self.ball.y <= self.right_paddle.y + PADDLE_HEIGHT - 1:  # ball touches paddle
                self.handle_paddle_collision(self.right_paddle)
                self.right_hits+=1
        elif self.left_paddle.x + PADDLE_WIDTH >= self.ball.x - (
                BALL_SIZE // 2):
            if self.left_paddle.y <= self.ball.y <= self.left_paddle.y + PADDLE_HEIGHT - 1:
                self.handle_paddle_collision(self.left_paddle)
                self.left_hits+=1

    def handle_paddle_collision(self, paddle):
        middle = (paddle.y + paddle.y + PADDLE_HEIGHT) // 2
        dist_difference = self.ball.y - middle
        if dist_difference >= 0:
            self.ball.y_speed += dist_difference * Y_AXIS_CHANGE

        else:
            self.ball.y_speed -= (-1) * dist_difference * Y_AXIS_CHANGE

        self.ball.x_speed *= -1
        # changing the the direction of the ball when hitting things

    def ball_wall_collision(self):
        if self.ball.y <= 0:
            self.ball.y_speed *= -1
        elif self.ball.y >= HEIGHT:
            self.ball.y_speed *= -1
        if self.ball.x <= 0:
            self.right_score += 1
            self.start_new_round()

        elif self.ball.x >= WIDTH:
            self.left_score += 1
            self.start_new_round()

        if (self.left_score or self.right_score) == MAX_POINTS:
            self.game_over = True

    def render_game(self):
        self.move_paddle()
        self.ball.move_ball()
        self.ball_peddle_collision()
        self.ball_wall_collision()
        game_info = GameInformation(
            self.left_hits, self.right_hits, self.left_score, self.right_score)
        return game_info

    def start_new_round(self):
        self.ball.y_speed = random.uniform(-3.5,3.5)
        self.ball.x_speed *= -1
        self.ball.x = self.ball.starting_x
        self.ball.y = self.ball.starting_y
        self.right_paddle.x = self.right_paddle.starting_x
        self.right_paddle.y = self.right_paddle.starting_y
        self.left_paddle.x = self.left_paddle.starting_x
        self.left_paddle.y = self.left_paddle.starting_y

    def end_game(self):
        if self.right_score == MAX_POINTS:

            self.display.draw_winner(self.display.screen, "Right")
        else:
            self.display.draw_winner(self.display.screen, "Left")

    def new_game(self):
        self.game_over = False
        self.start_new_round()
        self.right_score = 0
        self.left_score = 0


# def main():
#     running = True
#     clock = pygame.time.Clock()
#     game = Game()
#
#     while running:
#         clock.tick(60)
#         game.draw_all()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         if not game.game_over:
#             game.render_game()
#         else:
#             pygame.time.delay(5000)
#             game.new_game()
#     pygame.quit()
#
#
# if __name__ == '__main__':
#     main()
