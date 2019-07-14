import pygame
import game_functions as gf
from settings import Settings
from game_objects.ship import Ship


def run_game():
    # Init game and create a screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Initialize games objects
    ship = Ship(screen, settings)

    # Start main game loop
    while True:
        gf.check_events(ship)
        ship.update_position()
        gf.update_screen(screen, settings, ship)


run_game()
