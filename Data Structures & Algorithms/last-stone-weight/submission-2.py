class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while True:
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]

            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if abs(x - y): heapq.heappush_max(stones, abs(x - y))