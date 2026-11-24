class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        anc, size = list(range(n)), [1] * n
        def find(u):
            while anc[u] != u:
                anc[u] = anc[anc[u]]
                u = anc[u]
            return u
        res = [n]
        def union(u,v):
            u,v = find(u), find(v)
            if u != v:
                if size[v] > size[u]:
                    u,v = v,u
                anc[v] = u
                size[u] += size[v]
                res[0] -= 1
        for u,v in edges:
            union(u,v)
        return res[0]