# This is a sweep line problem -> sort the trips by startLocation
from typing import List
import functools

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carList = self.createList(trips)
        for [number, loc] in carList:
            capacity -= number
            print(number, loc, sep = ' ', end = '\n')
            if capacity < 0: 
                return False
        return True
        

    def createList(self, trips):
        res = []
        for i in range(len(trips)):
            res.append([trips[i][0], trips[i][1]])
            res.append([-trips[i][0], trips[i][2]])
        res.sort(key = functools.cmp_to_key(lambda a, b: a[1] - b[1] if a[1] != b[1] else a[0] - b[0]))
        return res

