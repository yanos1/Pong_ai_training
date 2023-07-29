import pygame

WHITE = (255, 255, 255)
RED = (200, 0, 0)
PINK = (200,153,255)

pygame.font.init()
SCORE_FONT = pygame.font.Font(None, 65)
BUTTON_FONT = pygame.font.SysFont("Ariel", 23)

# game assets #
pygame.display.set_caption('Pong')
PADDLE_IMAGE = pygame.image.load("Assets/paddle_improved.png")
BG_IMAGE = pygame.image.load("Assets/space_background.png")
TITLE_IMAGE = pygame.image.load("Assets/title_image.png")
BALL_IMAGE = pygame.image.load("Assets/Moon.png")
easy_mode_button_image = pygame.image.load("Assets/easy_mode_button.png")
hard_mode_button_image = pygame.image.load("Assets/hard_mode_button.png")
impossible_mode_button_image = pygame.image.load("Assets/impossible_mode_button.png")

easy_mode_text = BUTTON_FONT.render("Easy Mode", True, PINK)
hard_mode_text = BUTTON_FONT.render("Hard Mode", True, PINK)
impossible_mode_text = BUTTON_FONT.render("Impossible Mode", True,PINK)
impossible_but_text_loc = (13,13)
hard_but_text_loc = (32,13)
easy_but_text_loc = (32,13)


# button text locations #


class Display:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.screen = pygame.display.set_mode((width, height))
        self.score_font = SCORE_FONT
        self.impossible_but_loc = (self.width //2 - impossible_mode_button_image.get_width()//2, 450)
        self.hard_but_loc = (self.width // 2 - hard_mode_button_image.get_width() // 2, 350)
        self.easy_but_loc = (self.width // 2 - easy_mode_button_image.get_width() // 2, 250)

    def draw_screen(self, window, background):
        window.blit(background, (0, 0))

    def draw_title(self, window, title_image):
        window.blit(title_image, (self.width // 2 - title_image.get_width()//2, 20))

    def draw_buttons(self, window, em_button, hm_button, im_button):
        em_button.blit(easy_mode_text, easy_but_text_loc)
        window.blit(em_button, self.easy_but_loc)
        hm_button.blit(hard_mode_text,hard_but_text_loc)
        window.blit(hm_button, self.hard_but_loc)
        im_button.blit(impossible_mode_text,impossible_but_text_loc)
        window.blit(im_button, self.impossible_but_loc)

    def draw_score(self, window, score_left, score_right):
        score_r_text = self.score_font.render(f"{score_right}", True, self.color)
        window.blit(score_r_text, (self.width * 0.75, 10))

        score_l_text = self.score_font.render(f"{score_left}", True, self.color)
        window.blit(score_l_text, (self.width * 0.25, 10))

    def draw_hits(self, window, left_hits, right_hits):
        hits_text = self.score_font.render(
            f"{left_hits + right_hits}", True, RED)
        window.blit(hits_text, (self.width //
                                2 - hits_text.get_width() // 2, 10))

    def draw_winner(self, window, winner):
        winner_text = self.score_font.render(f"{winner} wins!", True, self.color)
        window.blit(winner_text, (self.width // 2.8, self.height // 2 - self.height // 8))

    def start_menu_ball_animation(self,start_ball):
        if start_ball.y <= 0:
            start_ball.y_speed *= -1
        elif start_ball.y >= self.height:
            start_ball.y_speed *= -1
        elif start_ball.x <= 0:
            start_ball.x_speed *= -1
        elif start_ball.x >= self.width:
            start_ball.x_speed *= -1




