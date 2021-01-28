import sys
import copy
from src.utils.parser import Parser
from src.data.puzzle import Puzzle
from src.algorithm.node import Node
from src.algorithm.a_star import a_star

if __name__ == "__main__":
    parser = Parser()
    
    try:
        if len(sys.argv) > 1:
            parser.open_file(sys.argv[1], "r")
            puzzle = Puzzle(parser.read_all_lines())
            node = Node(copy.deepcopy(puzzle))
            print("starting node :\n{}".format(node))
            a_star(node)
            parser.close_file()
        else:
            print("usage: please specfify a path")
    except Exception as error:
        print('Handling run-time error:', error)

# TODO solvable check