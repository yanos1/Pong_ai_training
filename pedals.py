WHITE = (255,255,255)
PEDAL_SPEED = 10


class Paddle:
    COLOR = WHITE
    SPEED = PEDAL_SPEED

    def __init__(self, x, y, width, height):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.width = width
        self.height = height

    def draw_paddle(self, window,image):
        window.blit(image, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.SPEED
        else:
            self.y += self.SPEED
