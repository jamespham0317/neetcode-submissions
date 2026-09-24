class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        treasure = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasure.append((r, c))

        visited = set()
        queue = collections.deque()
        for t in treasure:
            queue.append(t)

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if ((r, c) in visited or
                    r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    grid[r][c] == -1):
                    continue

                if grid[r][c] != 0:
                    grid[r][c] =  dist

                visited.add((r, c))

                queue.append((r + 1, c))
                queue.append((r - 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

            dist += 1