from typing import LiteralString





def readMaze(filePath: LiteralString):
    file = open(filePath)
    maze = file.readlines()
    print(maze[-1][-1])

    
readMaze("./maze1.txt")