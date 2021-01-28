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

    def generate_child(self, value_swaped: int, goal: Puzzle):
        child = copy.deepcopy(self)
        child.puzzle.swap_value(value_swaped)
        child.__g += 1
        child.update_score(goal)
        return child

    # TODO
    def __update_h(self, goal: Puzzle) -> None:
        self.__h = 0
        for i in range(len(goal.grid)):
            for j in range(len(goal.grid)):
                if self.puzzle.grid[i][j] != goal.grid[i][j]:
                    self.__h += 1

    # TODO
    def __update_f(self):
        self.__f = self.__g + self.__h

    # TODO
    def update_score(self, goal: Puzzle) -> None:
        self.__update_h(goal)
        self.__update_f()
