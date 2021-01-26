import sys
from src.utils.parser import Parser
    
if __name__ == "__main__":
    parser = Parser()
    
    try:
        if len(sys.argv) > 1:
            parser.open_file(sys.argv[1], "r")
            lines: list = parser.read_all_lines()
            for line in lines:
                print(line)
            parser.close_file()
        else:
            print("usage: please specfify a path")
    except Exception as error:
        print('Handling run-time error:', error)

