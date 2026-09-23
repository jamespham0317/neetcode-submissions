class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adjList = { i:[] for i in range(n)}
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for j in adjList[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        