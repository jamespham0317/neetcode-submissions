class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            diff = abs(first - second)
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        return stones[0] if stones else 0
        