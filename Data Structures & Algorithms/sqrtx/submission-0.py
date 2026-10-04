class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            m = -((-(r - l)) // 2) + l

            if m * m < x:
                l = m
            elif m * m > x:
                r = m - 1
            else:
                return m
        return l