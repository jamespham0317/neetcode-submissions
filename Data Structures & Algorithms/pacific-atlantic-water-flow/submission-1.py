class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        canReachPacific = set()
        canReachAtlantic = set()

        pacificQueue = collections.deque()
        atlanticQueue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0: 
                    pacificQueue.append((0, r, c))
                if r == rows - 1 or c == cols - 1:
                    atlanticQueue.append((0, r, c))

        pacificVisited = set()
        while pacificQueue:
            for i in range(len(pacificQueue)):
                prevHeight, r, c = pacificQueue.popleft()
                if (r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    (r, c) in pacificVisited or
                    prevHeight > heights[r][c]): 
                    continue
                pacificVisited.add((r, c))
                canReachPacific.add((r, c))
                pacificQueue.append((heights[r][c], r + 1, c))
                pacificQueue.append((heights[r][c], r - 1, c))
                pacificQueue.append((heights[r][c], r, c + 1))
                pacificQueue.append((heights[r][c], r, c - 1))

        atlanticVisited = set()
        while atlanticQueue:
            for i in range(len(atlanticQueue)):
                prevHeight, r, c = atlanticQueue.popleft()
                if (r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    (r, c) in atlanticVisited or
                    prevHeight > heights[r][c]): 
                    continue
                atlanticVisited.add((r, c))
                canReachAtlantic.add((r, c))
                atlanticQueue.append((heights[r][c], r + 1, c))
                atlanticQueue.append((heights[r][c], r - 1, c))
                atlanticQueue.append((heights[r][c], r, c + 1))
                atlanticQueue.append((heights[r][c], r, c - 1))

        res = []
        for n in canReachPacific:
            if n in canReachAtlantic:
                res.append([n[0], n[1]])

        return res