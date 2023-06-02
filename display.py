import pygame

WHITE = (255, 255, 255)
RED = (200,0,0)

class Display:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 65)

    def draw_screen(self, window, background):
        window.blit(background, (0, 0))

    def draw_score(self, window, score_left, score_right):
        score_r_text = self.font.render(f"{score_right}", True, self.color)
        window.blit(score_r_text, (self.width * 0.75, 10))

        score_l_text = self.font.render(f"{score_left}", True, self.color)
        window.blit(score_l_text, (self.width * 0.25, 10))

    def draw_hits(self,window,left_hits, right_hits):
        hits_text = self.font.render(
            f"{left_hits + right_hits}", True, RED)
        window.blit(hits_text, (self.width //
                                     2 - hits_text.get_width() // 2, 10))

    def draw_winner(self, window, winner):
        winner_text = self.font.render(f"{winner} wins!", True, self.color)
        window.blit(winner_text, (self.width // 2.8, self.height // 2 - self.height // 8))
