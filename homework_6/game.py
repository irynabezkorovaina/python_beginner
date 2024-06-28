from board import Board
from snake import Snake
from apple import Apple
from time import sleep
import random


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        snake_position = set(self.snake.body)
        for _ in range(self.width * self.height):
            new_i = random.randint(1, self.height - 2)
            new_j = random.randint(1, self.width - 2)
            new_position = (new_i, new_j)

            if new_position not in snake_position:
                self.apple = Apple(position=new_position)
                return
        raise GameOverError('No places for apple!')

    def clear(self):
        self.board = Board(self.width, self.height)

    def render(self):
        self.clear()

        head_i, head_j = self.snake.body[-1]
        self.board.board[head_i][head_j] = self.snake.head_symbol
        if len(self.snake.body) > 1:
            for section in self.snake.body[1:-1]:
                section_i, section_j = section
                self.board.board[section_i][section_j] = self.snake.symbol

        tail_i, tail_j = self.snake.body[0]
        if len(self.snake.body) > 1:
            self.board.board[tail_i][tail_j] = self.snake.tail_symbol

        # Place apple on the board
        apple_i, apple_j = self.apple.position
        self.board.board[apple_i][apple_j] = self.apple.symbol

        self.board.show()
        # sleep(1)

    def play(self):
        try:
            self.render()  # initial render of board, snake and apple
            while True:  # start our game
                snake_i, snake_j = self.snake.body[-1]
                if snake_i == 0 or snake_i == self.height - 1 or snake_j == 0 or snake_j == self.width - 1:
                    raise GameOverError('Snake hit the wall')

                possible_moves = self.snake.choices()
                if not possible_moves:
                    self.render()  # render last move
                    raise GameOverError('No moves for snake!')  # end the game

                next_move = None

                for move in possible_moves:
                    distance = Board.distance(move, self.apple.position)
                    if next_move is None or distance < Board.distance(next_move, self.apple.position):
                        next_move = move

                if next_move == self.apple.position:
                    self.snake.eat(next_move)  # eat apple
                    self.init_apple()  # init new apple
                    self.render()
                else:
                    self.snake.move(next_move)  # move the snake to the next valid position
                    self.render()

        except GameOverError as e:
            print(e)
            print('Game Over!')
