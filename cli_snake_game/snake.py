import curses

class Snake:
    def __init__(self, window: 'curses._CursesWindow', start_pos: tuple[int, int]):
        self.body = [start_pos]
        self.window = window

    def move(self, direction: str):
        y, x = self.body[0]

        if direction == 'UP':
            y -= 1
        elif direction == 'DOWN':
            y += 1
        elif direction == 'LEFT':
            x -= 1
        elif direction == 'RIGHT':
            x += 1

        self.body.insert(0, (y, x))

    def eat(self, food: 'Food'):
        if self.body[0] == food.get_position():
            food.generate()
            return True
        else:
            self.window.addch(self.body[-1][0], self.body[-1][1], ' ')
            self.body.pop()
            return False

    def check_collision(self):
        if (self.body[0] in self.body[1:]) or \
           (self.body[0][0] in [0, self.window.getmaxyx()[0]-1]) or \
           (self.body[0][1] in [0, self.window.getmaxyx()[1]-1]):
            return True
        return False

    def get_head_position(self):
        return self.body[0]
