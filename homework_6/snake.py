class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.head_symbol = '%'
        self.symbol = symbol
        self.tail_symbol = '^'
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)  # Remove the first element to simulate movement

    def choices(self):
        positions = []
        head_i, head_j = self.body[-1]
        potential_positions = {
            (head_i, head_j - 1),  # Left
            (head_i, head_j + 1),  # Right
            (head_i - 1, head_j),  # Up
            (head_i + 1, head_j)   # Down
        }
        for pos in potential_positions:
            if pos not in self.body:
                positions.append(pos)
        return positions
