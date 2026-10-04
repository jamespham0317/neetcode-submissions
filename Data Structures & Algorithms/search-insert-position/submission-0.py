class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) // 2 + l

            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return l