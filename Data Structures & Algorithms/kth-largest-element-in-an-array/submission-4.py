class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i, n in enumerate(nums):
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)
        