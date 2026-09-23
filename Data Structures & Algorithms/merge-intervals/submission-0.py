class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            last = res[-1]

            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                res.append(interval)
        return res