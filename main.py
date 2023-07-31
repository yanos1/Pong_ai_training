import pygame
import neat
import os
from trainAI import play_ai
from game import WIDTH, HEIGHT, WHITE
from display import Display, easy_mode_button_image, hard_mode_button_image, impossible_mode_button_image, BG_IMAGE, \
    TITLE_IMAGE, BALL_IMAGE
from ball import Ball

EASY = "easy"
HARD = "hard"
IMPOSSIBLE = "impossible"


def load_enemy(game_mode):
    """
    taking in a game mode and returning the right network for the game based on the game mode.
    :param game_mode: a game mode (easy, hard, impossible).
    :return: the compatible network for the game mode.
    """
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)  # can remove config since training is done.
    if game_mode == EASY:
        play_ai(config, EASY, "Neuron_networks/easiest_mode.pickle")
    if game_mode == HARD:
        play_ai(config, EASY, "Neuron_networks/hard_mode.pickle")
    if game_mode == IMPOSSIBLE:
        play_ai(config, EASY, "Neuron_networks/best.pickle")


def valid_mouse_click(button_pos, mouse_pos):
    """
    making sure we click within the given button
    :param button_pos: the position of the button.
    :param mouse_pos: the position of the mouse
    :return: True if the positions coincide, False otherwise.
    """
    if button_pos[0] <= mouse_pos[0] <= button_pos[0] + 150 and \
            button_pos[1] <= mouse_pos[1] <= button_pos[1] + 44:
        return True
    return False


def start_game():
    """
    This is the game start display, it will draw the start screen and buttons,
     waiting for a valid click to start the game.
    :return: the game mode being chosen
    """
    run = True
    start_display = Display(WIDTH, HEIGHT, WHITE)
    start_ball = Ball(WIDTH // 2, HEIGHT // 2)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        start_display.draw_screen(start_display.screen, BG_IMAGE)
        start_display.draw_title(start_display.screen, TITLE_IMAGE)
        start_display.draw_buttons(start_display.screen, easy_mode_button_image, hard_mode_button_image,
                                   impossible_mode_button_image)
        start_ball.draw_ball(start_display.screen, BALL_IMAGE)
        start_ball.move_ball()
        start_display.start_menu_ball_animation(start_ball)

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
