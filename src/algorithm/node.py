import copy
from enum import Enum
from src.data.puzzle import Puzzle

class Direction(Enum):
    RIGHT = 1,
    LEFT = 2,
    BOT = 3,
    TOP = 4

class Node:
    def __init__(self, puzzle: Puzzle):
        self.puzzle: Puzzle = puzzle
        self.__g: int = 0
        self.__h: int = 0
        self.__f: int = 0
        self.__update_score()

    def __str__(self):
        representation: str = "g = {}, h = {}, f = {}\n".format(self.__g, self.__h, self.__f)
        return (representation + self.puzzle.__str__())

    @property
    def g(self) -> int:
        return self.__g
    
    @property
    def h(self) -> int:
        return self.__h

    @property
    def f(self) -> int:
        return self.__f
    
    # TODO
    def __update_h(self):
        i: int = 0
        j: int = 0
        n: int = 1
        n_dir: int = -1
        max_dir: int = self.puzzle.size * 2 - 3
        index_max: int = self.puzzle.size - 1
        middle = self.puzzle.size / 2 + 1
        direction: Direction = Direction.RIGHT

        self.__h = 0
        while n_dir < max_dir:
            old_direction: Direction = copy.copy(direction)
            if self.puzzle.grid[i][j] != n:
                self.__h += 1
            if direction == Direction.RIGHT:
                if j == index_max:
                    direction = Direction.BOT
                else:
                    j += 1
            if direction == Direction.BOT:
                if i == index_max:
                    direction = Direction.LEFT
                else:
                    i += 1
            if direction == Direction.LEFT:
                if j == 0:
                    direction = Direction.TOP
                else:
                    j -= 1
            if direction == Direction.TOP:
                if i == 0:
                    direction = Direction.RIGHT
                else:
                    i -= 1
            n += 1
            if old_direction != direction:
                n_dir += 1
            if n_dir % 2 == 0 and n_dir != 0:
                index_max -= 1

    # TODO
    # def __update_f(self):

    # TODO
    def __update_score(self):
        self.__update_h()
