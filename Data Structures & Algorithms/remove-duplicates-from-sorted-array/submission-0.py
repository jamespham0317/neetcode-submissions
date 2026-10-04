class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        pos = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                k += 1
                nums[pos] = nums[i]
                pos += 1

        return k
            