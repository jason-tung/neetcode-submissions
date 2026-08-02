class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(a,b) for a,b in edges)
        current_path = deque()
        visited = set()
        d = [[] for _ in range(n + 1)]
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        def dfs(n, prev):
            current_path.append(n)
            visited.add(n)
            for k in d[n]:
                if k != prev: 
                    if k in visited:
                        current_path.append(k)
                        while current_path[0] != k:
                            current_path.popleft()
                        return current_path
                    child = dfs(k, n)
                    if child:
                        return child
            visited.remove(n)
            current_path.pop()
            return []
        ans = dfs(1, -1)
        sol = set()
        for i in range(len(ans) - 1):
            j = i + 1
            sol.add((ans[i], ans[j]))
        for (a,b) in edges[::-1]:
            if (a,b) in sol or (b,a) in sol:
                return [a,b]
        
            
                
