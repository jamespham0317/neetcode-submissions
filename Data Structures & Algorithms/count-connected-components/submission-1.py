class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(n1):
            res = n1
            while res != parent[res]:
                res = parent[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2: return 0
            
            parent[p2] = p1
            return 1

        res = n
        for e1, e2 in edges:
            res -= union(e1, e2)

        return res        