class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for n in nums:
            if n == val:
                continue
            nums[curr] = n
            curr += 1

        return curr 