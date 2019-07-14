import sys
import pygame


def check_events(ship):
    """Respond to keys events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ship)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)


def check_events_keydown(event, ship):
    """Respond to pressed keys"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True


def check_events_keyup(event, ship):
    """Respond to keys release"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False


def update_screen(screen, settings, ship):
    """Update images on the screen and flip to the new screen"""
    # Create background.
    screen.fill(settings.background_color)

    # Redraw ship
    ship.blit_me()

    # Make the most recently drawn screen visible
    pygame.display.flip()
