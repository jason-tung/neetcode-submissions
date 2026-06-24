class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edge_map = defaultdict(set)
        visited = set()
        for l in edges:
            edge_map[l[0]].add(l[1])
            edge_map[l[1]].add(l[0])
        def helper(i):
            visited.add(i)
            if not edge_map[i]:
                return 0
            total_cost = 0
            for node in edge_map[i]:
                if node not in visited:
                    child_cost = helper(node)
                    if hasApple[node] or child_cost != 0:
                        total_cost += 2
                    total_cost += child_cost
            return total_cost            
        return helper(0)