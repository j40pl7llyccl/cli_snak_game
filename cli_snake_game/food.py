import random
import curses

class Food:
    def __init__(self, window: 'curses._CursesWindow', max_y: int, max_x: int):
        self.position = (0, 0)
        self.window = window
        self.max_y = max_y
        self.max_x = max_x
        self.generate()

    def generate(self):
        y = random.randint(1, self.max_y - 2)
        x = random.randint(1, self.max_x - 2)
        self.position = (y, x)
        self.window.addch(self.position[0], self.position[1], '#')

    def get_position(self):
        return self.position
