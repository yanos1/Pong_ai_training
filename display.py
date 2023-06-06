import pygame

WHITE = (255, 255, 255)
RED = (200, 0, 0)
SCORE_FONT = pygame.font.Font(None, 65)
BUTTON_FONT = pygame.font.Font(None, 30)

# game assets #
pygame.display.set_caption('Pong')
PADDLE_IMAGE = pygame.image.load("paddle_improved.png")
BG_IMAGE = pygame.image.load("space_background.png")
BALL_IMAGE = pygame.image.load("Moon.png")
easy_mode_button_image = pygame.image.load("easy_mode_button.png")
hard_mode_button_image = pygame.image.load("hard_mode_button.png")
impossible_mode_button_image = pygame.image.load("impossible_mode_button.png")
easy_mode_text = BUTTON_FONT.render("Easy Mode", True, (255, 255, 255))
hard_mode_text = BUTTON_FONT.render("Hard Mode", True, (255, 255, 255))
impossible_mode_text = BUTTON_FONT.render("Impossible Mode", True, (255, 255, 255))

# button text locations #

easy_button_text_x = (easy_mode_button_image.get_width() - easy_mode_text.get_width()) // 2
easy_button_text_y = (easy_mode_button_image.get_height() - easy_mode_button_image.get_height()) // 2
hard_button_text_x = (hard_mode_button_image.get_width() - hard_mode_text.get_width()) // 2
hard_button_text_y = (hard_mode_button_image.get_height() - hard_mode_button_image.get_height()) // 2
impossible_button_text_x = (impossible_mode_button_image.get_width() - impossible_mode_text.get_width()) // 2
impossible_button_text_y = (impossible_mode_button_image.get_height() - impossible_mode_button_image.get_height()) // 2



class Display:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.screen = pygame.display.set_mode((width, height))
        self.score_font = SCORE_FONT
        self.impossible_but_loc = (self.width // 2 - impossible_mode_button_image.get_width() // 2, 400)
        self.hard_but_loc = (self.width // 2 - hard_mode_button_image.get_width() // 2, 300)
        self.easy_but_loc = (self.width // 2 - easy_mode_button_image.get_width() // 2, 200)

    def draw_screen(self, window, background):
        window.blit(background, (0, 0))

    def draw_title(self, window, title_image):
        window.blit(title_image, (self.width // 2 - title_image // 2 - title_image.get_width), 50)

    def draw_buttons(self, window, em_button, hm_button, im_button):
        window.blit(em_button, (self.width // 2 - em_button.get_width() // 2, 200))
        em_button.blit(easy_mode_text, (self.easy_but_loc[0],self.easy_but_loc[1]) )
        window.blit(hm_button, (self.width // 2 - hm_button.get_width() // 2, 300))
        hm_button.blit(hard_mode_text,(self.hard_but_loc[0],self.hard_but_loc[1]))
        window.blit(im_button, (self.width // 2 - im_button.get_width() // 2, 400))
        im_button.blit(impossible_mode_text,(self.impossible_but_loc[0],self.impossible_but_loc[1]))

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
