class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        map = {0 : 1}

        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k

            res += map.get(diff, 0)
            map[sum] = 1 + map.get(sum, 0)

        return res