class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        size, anc = [1] * n, list(range(n))
        def find(u):
            while u != anc[u]:
                anc[u] = anc[anc[u]]
                u = anc[u]
            return u
        def union(u,v):
            u,v = find(u), find(v)
            if u != v:
                if size[u] < size[v]:
                    u,v = v,u
                anc[v] = u
                size[u] += size[v]
        for u,v in edges:
            union(u,v)
        return len(set(find(u) for u in range(n)))