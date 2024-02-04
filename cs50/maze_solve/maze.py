from __future__ import annotations
from PIL import Image, ImageDraw

class Frame:
    def __init__(self, frame: list[list[str]]) -> None:
        self.frame = frame
    
    def set_char(self, axis_x: int, axis_y: int, char: str):
        self.frame[axis_y][axis_x] = char

    def get_string(self):
        return "\n".join(map(lambda element: "".join(element), self.frame))
    def get_char(self, x, y):
        return self.frame[y][x]
    
    def get_width(self):
        print(f'width {len(self.frame[0])}')
        return len(self.frame[0])
    
    def get_height(self):
        print(f'height {len(self.frame)}')
        return len(self.frame)

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

def drawMaze(frame: Frame, scale):
    real_width = frame.get_width() * scale + 1
    real_height = frame.get_height() * scale + 1

    canvas = (real_width, real_height)
    im = Image.new('RGBA', canvas, (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    fillMap = {
        "#": ((0,0,0),(255,255,255)),
        "S": ((0,128,0),(255,255,255)),
        "E": ((255,0,0),(255,255,255)),
        " ": ((255,255,255),(255,255,255))
    }

    for y in range(frame.get_height()):
        for x in range(frame.get_width()):
            print(f'drawing x {x} y {y}')
            x1 = scale * x
            x2 = scale * (x + 1)
            y1 = scale * y
            y2 = scale * (y + 1)
            draw.rectangle((x1, y1, x2, y2), fill=fillMap[frame.get_char(x,y)][0], outline=fillMap[frame.get_char(x,y)][1])
    im.save("./maze.png")

def readMaze(filePath: str):
    file = open(filePath)
    maze: list[str] = list(map(lambda line: line.rstrip('\n') ,file.readlines()))
    print(f'maze width {len(maze[0])}')
    print(f'maze height {len(maze)}')

    frame = Frame(maze)

    drawMaze(frame, 10)

    
readMaze("./maze1.txt")