from heapq import heappop,heappush
class Solution:
    # From [0, 0] to [m - 1, n - 1] the minimum cost
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        loc = []
        de = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        row, col = len(A), len(A[0])
        heappush(loc, [A[0][0], 0, 0])
        visited = [[False for _ in range(row)] for _ in range(col)]
        while len(loc) != 0:
            dis, x, y = heappop(loc)
            visited[x][y] = True
            if x == row - 1 and y == col - 1: return dis
            for i in range(4):
                newx, newy = x + de[i][0], y + de[i][1]
                if newx >= 0 and newx < row and newy >= 0 and newy < col and visited[newx][newy] == False:
                    newdis = dis + A[newx][newy]
                    heappush(loc, [newdis, newx, newy])
        return -1
                


