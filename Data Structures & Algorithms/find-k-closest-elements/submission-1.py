class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        l, r = 0, len(arr) - 1

        while l < r:
            m = l + (r - l) // 2

            if arr[m] < x:
                l = m + 1
            else:
                r = m

        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[r] - x) < abs(arr[l] - x):
                r += 1
            else:
                l -= 1

        return arr[l + 1: r]