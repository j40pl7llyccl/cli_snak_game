import curses
from snake import Snake
from food import Food
from score import Score

class Game:
    def __init__(self):
        self.score = Score()
        self.window = curses.initscr()
        self.window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.window.border(0)
        self.window.nodelay(1)
        self.max_y, self.max_x = self.window.getmaxyx()
        self.snake = Snake(self.window, (self.max_y//2, self.max_x//2))
        self.food = Food(self.window, self.max_y, self.max_x)

    def run(self):
        key = curses.KEY_RIGHT
        while True:
            self.window.border(0)
            self.window.addstr(0, 2, 'Score: ' + str(self.score.get_score()) + ' ')
            self.window.timeout(150 - (len(self.snake.body)//5 + len(self.snake.body)//10)%120)

            event = self.window.getch()
            key = key if event == -1 else event

            self.snake.move('UP' if key == curses.KEY_UP else
                            'DOWN' if key == curses.KEY_DOWN else
                            'LEFT' if key == curses.KEY_LEFT else
                            'RIGHT')

            if self.snake.check_collision():
                self.end_game()
                break

            if self.snake.eat(self.food):
                self.score.increment()

            self.window.addch(self.snake.get_head_position()[0], self.snake.get_head_position()[1], '*')

    def end_game(self):
        self.window.addstr(self.max_y//2, (self.max_x-len('Game Over!'))//2, 'Game Over!')
        self.window.refresh()
        curses.napms(2000)
        curses.endwin()
