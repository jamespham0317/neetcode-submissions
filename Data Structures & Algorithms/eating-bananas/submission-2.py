class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (r - l) // 2 + l

            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(p / k)

            if hoursTaken <= h: 
                res = k
                r = k - 1
            else: 
                l = k + 1

        return res