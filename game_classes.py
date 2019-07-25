from libraries import *

# TODO: Make a player class and have two child classes for a hider and seeker.
# Just a square block for now.
class Player(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height):
        super().__init__()

        self.side_length = 30

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(SILVER)
        self.rect = self.image.get_rect()

        self.display_width = display_width
        self.display_height = display_height

        self.rect.x = self.display_width + self.side_length
        self.rect.y = random.randrange(0, self.display_height)

        self.vertical_momentum = 0
        self.horizontal_momentum = 0

    def jump(self):
        self.vertical_momentum += 30

    def ground_check(self):
        if self.vertical_momentum < 0:
            if ((self.rect.y - self.side_length) - self.vertical_momentum) < 0: 
                self.reduce_momentum_value = abs((self.rect.y - self.side_length)
                    - self.vertical_momentum)
                self.vertical_momentum += self.reduce_momentum_value

    def update(self):
        self.ground_check()

        self.rect.x += self.horizontal_momentum
        self.rect.y += self.vertical_momentum

        if self.rect.y != 0 or (self.rect.y + self.vertical_momentum) != 0:
            self.vertical_momentum -= 5
        else:
            pass
