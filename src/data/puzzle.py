from typing import List
import copy

class Puzzle:
    def __init__(self, puzzle: List[str] = None):
        self.grid: List[List[int]] = list()
        self.__size: int = 0
        for line in puzzle:
            line.strip()
            if line[0] != '#':
                if self.__size == 0:
                    self.__size = int(line)
                else:
                    integer_line = [int(n) for n in line.replace(' ', '')]
                    self.grid.append(integer_line)

    def __str__(self):
        representation: str = ""
        line: str
        for line in self.grid:
            representation += ' '.join([str(elem) for elem in line])
            representation += '\n'
        return representation

    @property
    def size(self) -> int:
        return self.__size

    def get_case_indexes(self, value: int) -> tuple:
        i: int = 0
        while i < self.size:
            j: int = 0
            while j < self.size:
                if self.grid[i][j] == value:
                    return i, j
                j += 1
            i += 1
        raise RuntimeError("In get_case_indexes : Impossible to find value {}".format(value))

    def swap_value(self, value_swaped: int) -> tuple:
        i_empty, j_empty = self.get_case_indexes(0)
        i_swaped, j_swaped = self.get_case_indexes(value_swaped)
        self.grid[i_empty][j_empty] = self.grid[i_swaped][j_swaped]
        self.grid[i_swaped][j_swaped] = 0
        return i_swaped, j_swaped

    # def generate_new_instance(self, value_swaped: int) -> Puzzle:
    #     i_empty: int = 0
    #     j_empty: int = 0
    #     i_swaped: int = 0
    #     j_swaped: int  = 0
    #     with self.get_case_indexes(0) as indexes:
    #         i_empty = indexes[0]
    #         j_empty = indexes[1]
    #     with self.get_case_indexes(value_swaped) as indexes:
    #         i_swaped = indexes[0]
    #         j_swaped = indexes[1]
    #     new_instance: Puzzle = copy.deepcopy(self)
    #     new_instance.grid[i_empty][j_empty] = self.grid[i_swaped][j_swaped]
    #     new_instance.grid[i_swaped][j_swaped] = 0
    #     return new_instance