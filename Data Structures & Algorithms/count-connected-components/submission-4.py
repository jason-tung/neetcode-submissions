class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ancestor = list(range(n))
        size = [1] * n
        def find(u):
            while u != ancestor[u]:
                ancestor[u] = ancestor[ancestor[u]]
                u = ancestor[u]
            return u
        def union(u,v):
            nonlocal n
            ua, va = find(u), find(v)
            if ua != va:
                n -= 1
                if size[ua] < size[va]:
                    ua, va = va, ua
                size[ua] += size[va]
                ancestor[va] = ua
        for u,v in edges:
            union(u,v)
        return n
