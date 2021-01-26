from typing import List
import sys

class Parser:
    def __init__(self):
        self.file = None

    def open_file(self, file_path: str, mode: str) -> None:
        self.file = open(file_path, mode)

    def close_file(self) -> None:
        if self.file:
            self.file.close()
        else:
            raise RuntimeError("no open file")

    def read_file(self) -> str:
        if self.file:
            return self.file.read()
        raise RuntimeError("no open file")

    def read_next_line(self) -> str:
        if self.file:
            return self.file.readline()
        raise RuntimeError("no open file")

    def read_all_lines(self) -> list:
        if self.file:
            lines = self.file.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]
            return lines
        raise RuntimeError("no open file")
