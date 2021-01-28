from typing import List
from src.algorithm.node import Node
from src.data.puzzle import Puzzle
from operator import attrgetter

def expand_node(node: Node, opened: List[Node], closed: List[Node], goal: Puzzle) -> None:
    i_empty, j_empty = node.puzzle.get_case_indexes(0)
    children: List[Node] = list()
    if j_empty + 1 < node.puzzle.size:
        children.append(node.generate_child(node.puzzle.grid[i_empty][j_empty + 1], goal))
    if j_empty - 1 > 0:
        children.append(node.generate_child(node.puzzle.grid[i_empty][j_empty - 1], goal))
    if i_empty + 1 < node.puzzle.size:
        children.append(node.generate_child(node.puzzle.grid[i_empty + 1][j_empty], goal))
    if i_empty - 1 > 0:
        children.append(node.generate_child(node.puzzle.grid[i_empty - 1][j_empty], goal))
    for child in children:
        if child not in opened and child not in closed:
            opened.append(child)
    opened.remove(node)
    closed.append(node)

def make_goal(s) -> List[str]:
    ts = s*s
    str_puzzle = [-1 for i in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        str_puzzle[x + y*s] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == s or x + ix < 0 or (ix != 0 and str_puzzle[x + ix + y*s] != -1):
            iy = ix
            ix = 0
        elif y + iy == s or y + iy < 0 or (iy != 0 and str_puzzle[x + (y+iy)*s] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == ts:
            cur = 0
    puzzle: List[str] = [str(s)]
    puzzle += [str_puzzle[i * s: (i + 1) * s] for i in range(s)]
    for i in range(1, s + 1):
        puzzle[i] = " ".join(str(elem) for elem in puzzle[i])
    return puzzle

def select_best_node(nodes: List[Node]) -> Node:
    return min(nodes, key=attrgetter('f'))

def a_star(starting_node: Node):
    goal: Puzzle = Puzzle(make_goal(starting_node.puzzle.size))
    opened: List[Node] = list()
    closed: List[Node] = list()
    success: bool = False

    starting_node.update_score(goal)
    opened.append(starting_node)
    selected_node: Node = None
    while len(opened) and success == False:
        selected_node = select_best_node(opened)
        if selected_node.puzzle == goal:
            success = True
        else:
            expand_node(selected_node, opened, closed, goal)
    print("Result = ")
    print(selected_node)