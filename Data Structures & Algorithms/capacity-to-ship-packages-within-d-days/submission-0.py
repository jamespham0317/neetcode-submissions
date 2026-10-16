class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def numShips(capacity):
            ships = 1
            currCapacity = capacity
            for w in weights:
                if currCapacity - w < 0:
                    ships += 1
                    currCapacity = capacity - w
                else:
                    currCapacity -= w
            return ships

        while l < r:
            m = (r - l) // 2 + l

            if numShips(m) <= days:
                r = m
            else:
                l = m + 1

        return l
        