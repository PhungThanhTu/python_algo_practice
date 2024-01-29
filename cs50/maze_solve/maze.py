from __future__ import annotations

class Frame:
    def __init__(self, frame: list[list[str]]) -> None:
        self.frame = frame
    
    def set_char(self, axis_x: int, axis_y: int, char: str):
        self.frame[axis_y][axis_x] = char

    def get_string(self):
        return "\n".join(map(lambda element: "".join(element), self.frame))

class Node:
    def __init__(self, location: tuple, parent: Node, cost: int) -> None:
        self.location = location
        self.parent = parent
        self.cost = cost
        
class Path:
    def __init__(self, root: Node) -> None:
        self.path_map[root.location] = root
    def add_node(self, node: Node) -> None:
        self.path_map[node.location] = node
    def get_node(self, location: tuple[int, int]) -> Node:
        return self.path_map[location]
    
def readMaze(filePath: str):
    file = open(filePath)
    maze = file.readlines()
    frame = Frame(maze)
    print(frame.get_string())

    
readMaze("./maze1.txt")