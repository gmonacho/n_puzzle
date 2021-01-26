class Puzzle:
    def __init__(self, puzzle: list):
        self.grid = list()
        self.size = 0
        for line in puzzle:
            line.strip()
            if line[0] != '#':
                if self.size != 0:
                    self.size = str(line)
                else:
                    self.grid.append(line.split(' '))

    # def __str__(self):