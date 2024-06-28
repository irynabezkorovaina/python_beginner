class Color:
    """
    ANSI Colors for terminal
    """
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'
    PINK: str = '\033[38;5;206m'


class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    def init_board(self):
        board = []
        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.border] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.border)
                    else:
                        row.append(' ')
                board.append(row)
        return board

    @staticmethod
    def colored(symbol: str) -> str:
        if symbol == '*':
            return f'{Color.WARNING}{symbol}{Color.ENDC}'
        elif symbol == '@':
            return f'{Color.FAIL}{symbol}{Color.ENDC}'
        elif symbol == 'o':
            return f'{Color.OKGREEN}{symbol}{Color.ENDC}'
        elif symbol == '^':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        elif symbol == '%':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        else:
            return symbol

    def clear(self):
        self.board = self.init_board()

    def show(self):
        for row in self.board:
            colored_row = [self.colored(symbol) for symbol in row]
            print(''.join(colored_row))

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return (p1_i - p2_i) ** 2 + (p1_j - p2_j) ** 2
