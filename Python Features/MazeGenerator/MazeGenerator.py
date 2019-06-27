# Maze Generator -> DFS method to generate a maze ->
# Key: Create a Maze with odd length and odd width.
#       For every (2i, 2j) point, you can access by the path you generate for DFS method.
#       Lets say you have reached the point c below:
#           ...      ...         ...
#           0 0 0 0 c ? p x x 
#           x x x x ? x x x x
#           x x x x p x x x x
#       In DFS iteration for point c, you should randomly choose two potencial point to
#       continue creating path. Lets say you choose to go down.
#           0 0 0 0 0 x x x x 
#           x x x x 0 x x x x
#           x x p ? c ? p x x
#       Then next state you filled two more point and have two more candidates to choose.

import random
from typing import List

class MazeGenerator:
    __transX = [-1, 1, 0, 0]
    __transY = [0, 0, -1, 1]

    def createMaze(self, length: int, width: int) -> List[List[bool]]: 
        if length <= 0 or width <= 0: 
            return [[]]

        maze = [[False for _ in range(2 * length + 1)] for _ in range(2 * width + 1)]
        start, end = 0, 0
        maze[start][end] = True
        self.__DFS(maze, start, end)
        return maze
        
    def __inBound(self, x: int, y: int, maze: List[List[bool]]) -> None:
        return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])

    def __DFS(self, maze: List[List[bool]], x: int, y: int) -> None:
        matrixLength = len(maze)
        matrixWidth = len(maze[0])
        directionVisited = [False for _ in range(4)]
        while True:
            i = random.randint(0, 3)
            if directionVisited == [True, True, True, True]: 
                return
            if directionVisited[i] == True:
                continue

            newX = x + self.__transX[i] * 2
            newY = y + self.__transY[i] * 2
            intersectionX = x + self.__transX[i]
            intersectionY = y + self.__transY[i]
            
            directionVisited[i] = True

            if self.__inBound(newX, newY, maze) and not maze[newX][newY]:
                maze[newX][newY] = True
                maze[intersectionX][intersectionY] = True
                self.__DFS(maze, newX, newY)
            
    def printMaze(self, length: int, width: int) -> None: 
        maze = self.createMaze(length, width)
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                print('O' if maze[i][j] == True else 'X', end = ' ')
            print()


MazeGenerator().printMaze(2,3)
print()
MazeGenerator().printMaze(4,5)
