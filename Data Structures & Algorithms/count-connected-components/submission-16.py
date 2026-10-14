class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        size = [1] * n
        anc = list(range(n))
        def find(u):
            if u != anc[u]:
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
        for u,v in edges:
            union(u,v) 
        return len(set(find(u) for u in anc))