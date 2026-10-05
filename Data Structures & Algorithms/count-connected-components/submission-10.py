class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        anc, size = list(range(n)), [1] * n
        def find(u):
            while u != anc[u]:
                anc[u] = anc[anc[u]]
                u = anc[u]
            return u
        def union(u,v):
            u,v = find(u), find(v)
            if u != v:
                if size[u] < size[v]:
                    v, u = u, v
                anc[v] = u
                size[u] += size[v]
                return 1
            return 0
        for u,v in edges:
            n -= union(u,v)
        return n
        