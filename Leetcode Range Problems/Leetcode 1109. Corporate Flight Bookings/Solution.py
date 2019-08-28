class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        for start, end, h in bookings:
            res[start - 1] += h
            res[end] -= h
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:-1]