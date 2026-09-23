class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            map[n] += 1
        for n, c in map.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) == k:
                    return result
        