class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        self.fresh = 0
        rotten = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: self.fresh += 1
                if grid[r][c] == 2: rotten.append((r, c))

        def rot(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != 1):
                return

            grid[r][c] = 2
            rotten.append((r, c))
            self.fresh -= 1

        while self.fresh and rotten:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            res += 1

        if self.fresh != 0: return -1
        return res
        