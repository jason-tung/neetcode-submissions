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
                if size[v] > size[u]:
                    u,v = v,u
                size[u] += size[v]
                anc[v] = u
                return 1
            return 0
        return n - sum(union(u,v) for u,v in edges)