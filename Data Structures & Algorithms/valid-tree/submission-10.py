class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = [[] for _ in range(n)]
        for (a,b) in edges:
            d[a].append(b)
            d[b].append(a)
        visited = [False for _ in range(n)]
        q = deque([(0,-1)])
        visited[0] = True
        while q:
            n,prev = q.popleft()
            for k in d[n]:
                if k != prev:
                    if visited[k]:
                        return False
                    visited[k] = True
                    q.append((k, n))
        return all(visited)
            