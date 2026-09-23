class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if (r + dr < rows and 
                        r + dr >= 0 and
                        c + dc < cols and
                        c + dc >= 0 and
                        grid[r + dr][c + dc] == 1):
                        grid[r + dr][c + dc] = 2
                        queue.append([r + dr, c + dc])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1