class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(a,b) for a,b in edges)
        d = [[] for _ in range(n + 1)]
        ind =[0] * (n + 1)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
            ind[a] += 1
            ind[b] += 1
        q = deque(k for k in range(n + 1) if ind[k] == 1)
        while q:
            p = q.pop()
            for k in d[p]:
                ind[k] -= 1
                if ind[k] == 1:
                    q.append(k)
        looped_nodes = set(k for k in range(n + 1) if ind[k] >= 2)
        for (a,b) in edges[::-1]:
            if a in looped_nodes and b in looped_nodes:
                return [a,b]
                
