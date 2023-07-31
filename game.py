import pygame
import random
from display import Display, BALL_IMAGE, BG_IMAGE, PADDLE_IMAGE
from ball import Ball
from pedals import Paddle

pygame.init()

##  game settings ##
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
Y_AXIS_CHANGE = 0.07
MAX_POINTS = 7
WHITE = (255, 255, 255)

EASY = "easy"
HARD = "hard"
IMPOSSIBLE = "impossible"


########################


class GameInformation:
    """
    This class will be used to track down relevant information for the network to take in.
    """
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score


class Game:
    """
    This class is in charge of game logic and game flow
    """
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.set_game_settings()  # alter peddle speed, and max points needed to win.
        self.display = Display(WIDTH, HEIGHT, BACKGROUND_COLOR) # Display object
        self.ball = Ball(WIDTH // 2, HEIGHT // 2)  # Ball object
        self.left_paddle = Paddle(right_paddle_x, right_paddle_y, PADDLE_WIDTH,
                                  PADDLE_HEIGHT, self.left_paddle_speed)
        self.right_paddle = Paddle(left_paddle_x, left_paddle_y, PADDLE_WIDTH,
                                   PADDLE_HEIGHT, self.right_paddle_speed)
        self.right_score = 0
        self.right_hits = 0
        self.left_score = 0
        self.left_hits = 0
        self.game_over = False

    def set_game_settings(self):
        """
        alters the settings based on the level chosen by the user
        """
        if self.game_mode == IMPOSSIBLE:
            self.player_max_points = 1  # in impossible mode, human only need 1 point to win.
        else:
            self.player_max_points = MAX_POINTS
        if self.game_mode == HARD:
            self.right_paddle_speed = 7
        else:
            self.right_paddle_speed = 10
        self.left_paddle_speed = 10

    def draw_all(self):
        """
        using the Display object to draw the game
        :return:
        """
        self.display.draw_screen(self.display.screen, BG)
        self.display.draw_score(self.display.screen, self.left_score,
                                self.right_score)
        self.display.draw_hits(self.display.screen, self.left_hits, self.right_hits)
        self.ball.draw_ball(self.display.screen, BALL_IMAGE)
        self.right_paddle.draw_paddle(self.display.screen, PADDLE_IMAGE)
        self.left_paddle.draw_paddle(self.display.screen, PADDLE_IMAGE)
        if self.game_over:
            self.end_game()
        pygame.display.update()

    def move_paddle(self, left=True, up=True):
        """
        Move the left or right paddle.
        :returns: boolean indicating if paddle movement is valid.
                  Movement is invalid if it causes paddle to go
                  off the screen
        """
        if left:
            if up and self.left_paddle.y - self.left_paddle.speed < 0:
                return False
            if not up and self.left_paddle.y + PADDLE_HEIGHT > self.display.height:
                return False
            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - self.right_paddle.speed < 0:
                return False
            if not up and self.right_paddle.y + PADDLE_HEIGHT > self.display.height:
                return False
            self.right_paddle.move(up)

        return True

    def ball_peddle_collision(self):
        """
        This function will detect ball-paddle collision.
        :return: "left" if the left peddle hit the ball, "right" if the right peddle hit the ball
        """
        if self.right_paddle.x + 1 == self.ball.x + (
                BALL_SIZE // 2):
            if self.right_paddle.y <= self.ball.y <= self.right_paddle.y + PADDLE_HEIGHT + 5:  # ball touches paddle
                self.handle_paddle_collision(self.right_paddle)
                return "right"

        elif self.left_paddle.x + PADDLE_WIDTH == 1 + self.ball.x - (
                BALL_SIZE // 2):
            if self.left_paddle.y <= self.ball.y <= self.left_paddle.y + PADDLE_HEIGHT + 5:
                self.handle_paddle_collision(self.left_paddle)
                return "left"

    def handle_paddle_collision(self, paddle):
        """
        This function changes ball trajectory based on collisions with a paddle.
        :param paddle: the paddle which hit the ball
        """
        middle = (paddle.y + paddle.y + PADDLE_HEIGHT) // 2
        dist_difference = self.ball.y - middle
        if dist_difference >= 0:
            self.ball.y_speed += dist_difference * Y_AXIS_CHANGE

        else:
            self.ball.y_speed += dist_difference * Y_AXIS_CHANGE

        self.ball.x_speed *= -1
        # changing the the direction of the ball when hitting things

    def ball_wall_collision(self):
        """
        this function changes ball trajectory based on collision with a wall.
        if it is one of the players wall, then a point is given and the game resets.
        """
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

        if self.left_score == MAX_POINTS or self.right_score == self.player_max_points:
            self.game_over = True

        elif self.ball.x >= WIDTH:
            self.left_score += 1
            self.start_new_round()


    def move_ball_and_detect_collision(self):
        """
        initiating ball movement and checking ball-paddle collision using an earlier function
        :return:
        """
        self.ball.move_ball()
        hit = self.ball_peddle_collision()
        if hit == "left":
            self.left_hits += 1
        elif hit == "right":
            self.right_hits += 1

        self.ball_wall_collision()


    def start_new_round(self):
        self.ball.y_speed = random.choice([-2.3, 2.3])  # ball will not move straight with this line when the round starts.
        self.ball.x_speed *= -1
        self.ball.x = self.ball.starting_x
        self.ball.y = self.ball.starting_y
        self.right_paddle.x = self.right_paddle.starting_x
        self.right_paddle.y = self.right_paddle.starting_y
        self.left_paddle.x = self.left_paddle.starting_x
        self.left_paddle.y = self.left_paddle.starting_y

    def end_game(self):
        """
        checking whether a player won.
        """
        if self.right_score == MAX_POINTS:

            self.display.draw_winner(self.display.screen, "Right")
        elif self.left_score == self.player_max_points:
            self.display.draw_winner(self.display.screen, "Left")

    def new_game(self):
        self.game_over = False
        self.start_new_round()
        self.right_score = 0
        self.left_score = 0
        self.left_hits = self.right_hits = 0
