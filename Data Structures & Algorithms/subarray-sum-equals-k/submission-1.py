class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        suffix = {0 : 1}

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k

            res += suffix.get(diff, 0)
            suffix[sum] = 1 + suffix.get(sum, 0)

        return res