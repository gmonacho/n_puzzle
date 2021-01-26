from typing import List

class Puzzle:
    def __init__(self, puzzle: List[str]):
        self.grid: List[str] = list()
        self.__size: int = 0
        for line in puzzle:
            line.strip()
            if line[0] != '#':
                if self.__size == 0:
                    self.__size = int(line)
                else:
                    self.grid.append(line)

    def __str__(self):
        representation: str = ""
        line: str
        for line in self.grid:
            representation += line + '\n'
        return representation

    @property
    def size(self) -> int:
        return self.__size