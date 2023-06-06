import pygame
import neat
import os
from trainAI import play_ai
from pong import WIDTH, HEIGHT, WHITE
from display import Display, easy_mode_button_image, hard_mode_button_image, impossible_mode_button_image, BG_IMAGE

EASY = "easy"
HARD = "hard"
IMPOSSIBLE = "impossible"



def load_enemy(game_mode):
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_path)
    if game_mode == EASY:
        play_ai(config,EASY,"easiest_mode.pickle")
    if game_mode == HARD:
        play_ai(config,EASY,"hard_mode.pickle")
    if game_mode == IMPOSSIBLE:
        play_ai(config,EASY,"best.pickle")


def valid_mouse_click(button_pos, mouse_pos):
    if button_pos[0] <= mouse_pos[0] <= button_pos[0] + 150 and \
            button_pos[1] <= mouse_pos[1] <= button_pos[1] + 44:
        return True
    return False


def start_game():
    run = True
    start_display = Display(WIDTH, HEIGHT, WHITE)
    while run:
        start_display.draw_screen(start_display.screen, BG_IMAGE)
        start_display.draw_title(start_display.screen, "title_image.png")
        start_display.draw_buttons(start_display.screen, easy_mode_button_image, hard_mode_button_image,
                                   impossible_mode_button_image)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if valid_mouse_click(start_display.easy_but_loc, mouse_pos):
                    return EASY
                elif valid_mouse_click(start_display.hard_but_loc, mouse_pos):
                    return HARD
                elif valid_mouse_click(start_display.impossible_but_loc, mouse_pos):
                    return IMPOSSIBLE

            # Quit the game
            pygame.quit()


def play_game():
    game_mode = start_game()
    if game_mode == EASY:
        load_enemy(EASY)
    elif game_mode == HARD:
        load_enemy(HARD)
    elif game_mode == IMPOSSIBLE:
        load_enemy(IMPOSSIBLE)


if __name__ == '__main__':
    play_game()
