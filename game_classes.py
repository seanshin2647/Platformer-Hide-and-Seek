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

        self.rect.x = random.randrange(0, self.display_height)
        self.rect.y = self.display_height - self.side_length 

        self.vertical_momentum = 0
        self.horizontal_momentum = 0

        self.jumps_left = 2

    def jump(self):
        if self.jumps_left > 0:
            self.vertical_momentum = -13
            self.jumps_left -= 1

    def left(self):
        self.horizontal_momentum -= 10

    def right(self):
        self.horizontal_momentum += 10

    def slow_momentum_left(self):
        self.horizontal_momentum += 10

    def slow_momentum_right(self):
        self.horizontal_momentum -= 10

    def vertical_boundary_check(self):
        if self.vertical_momentum > 0:
            if self.rect.y + self.side_length + self.vertical_momentum > self.display_height:
                self.reduce_momentum_value = (self.rect.y + self.side_length +
                    self.vertical_momentum) - self.display_height
                self.vertical_momentum -= self.reduce_momentum_value

    def horizontal_boundary_check(self):
        if self.horizontal_momentum < 0:
            if self.rect.x + self.horizontal_momentum < 0:
                self.reduce_horizontal_momentum = abs(0 - (self.rect.x + 
                    self.vertical_momentum))
                self.horizontal_momentum += self.reduce_horizontal_momentum
        elif self.horizontal_momentum > 0:
            if self.rect.x + self.side_length + self.horizontal_momentum > self.display_width:
                self.reduce_horizontal_momentum = (self.rect.x + self.side_length +
                    self.horizontal_momentum - self.display_width)
                self.horizontal_momentum -= self.reduce_horizontal_momentum

    def update(self):
        self.vertical_boundary_check()
        self.horizontal_boundary_check()

        self.rect.x += self.horizontal_momentum
        self.rect.y += self.vertical_momentum

        if self.rect.y == self.display_height - self.side_length:
            self.vertical_momentum = 0
        elif self.vertical_momentum < 13:
                # TODO: Change this to make the jump look smoother.
                self.vertical_momentum += 1

        # TODO: Change this so that the player will new jumps when they land on a platform.
        # Possible set it so that whenever vertical_momentum is == to 0, it resets.
        if self.rect.y == self.display_height - self.side_length:
            self.jumps_left = 2