from game_states import *

pygame.init()

FPS = 60
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    # TODO: Add a dedicated state manager for this.
    game_state = Game_State(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    
    while True:
        # Temporary fix. The player's model for some reason does not update as 
        # it should and smears across the screen. This fixes that, though in
        # a messy way.
        DISPLAY.fill(BLACK)

        pressed_buttons = pygame.key.get_pressed()
        game_state.handle_events(pressed_buttons, DISPLAY_WIDTH, DISPLAY_HEIGHT)

        game_state.update()

        game_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()