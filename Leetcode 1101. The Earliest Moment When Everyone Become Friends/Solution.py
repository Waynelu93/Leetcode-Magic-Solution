# This is a typical union find problem
from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        people = {x: x for x in range(N)}
        self.mergeTime = N - 1

        def merge(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                people[fx] = fy
                self.mergeTime -= 1
        
        def find(x):
            if people[x] != x:
                people[x] = find(people[x])
            return people[x]
                
        for t,x,y in sorted(logs):
            merge(x,y)
            if self.mergeTime == 0:
                return t
        return -1
                

logs, N = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6
print(Solution().earliestAcq(logs, N))
