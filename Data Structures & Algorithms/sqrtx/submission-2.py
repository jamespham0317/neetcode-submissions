class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l < r:
            m = l + -(-(r - l) // 2)
            square = m * m
            if square > x:
                r = m - 1
            else:
                l = m

        return l

            