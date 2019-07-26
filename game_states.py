from game_classes import *

def kill_game():
    pygame.quit()
    quit()

class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

class Game_State(State):
    def __init__(self, display_width, display_height):
        super().__init__()

        self.all_sprites_list = pygame.sprite.Group()

        self.player_one = Player(display_width, display_height)
        self.all_sprites_list.add(self.player_one)

# Core function.
    def render(self, display):
        self.all_sprites_list.draw(display)
#

# Core function.
    def update(self):
        self.all_sprites_list.update()
#

# Core function.
    def handle_events(self, pressed_buttons, display_width, display_height):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()

            if pressed_buttons[pygame.K_w]:
                self.player_one.jump()
            elif pressed_buttons[pygame.K_a]:
                self.player_one.left()
#