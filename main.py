import sys
import copy
from src.utils.parser import Parser
from src.data.puzzle import Puzzle
from src.algorithm.node import Node

if __name__ == "__main__":
    parser = Parser()
    
    try:
        if len(sys.argv) > 1:
            parser.open_file(sys.argv[1], "r")
            puzzle = Puzzle(parser.read_all_lines())
            node = Node(copy.copy(puzzle))
            try:
                print(node, end='')
            except Exception as error:
                print(error)
            parser.close_file()
        else:
            print("usage: please specfify a path")
    except Exception as error:
        print('Handling run-time error:', error)


# TODO convert puzzle grid to integer grid
# TODO solvable check