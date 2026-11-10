class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        visited = set()
        n = len(nums)
        def dfs(i):
            if i not in visited:
                cur.append(nums[i])
                visited.add(i)
                if len(cur) < n:
                    for j in range(n):
                        if j not in visited:
                            dfs(j)
                else:
                    res.append([*cur])
                visited.remove(i)
                cur.pop()
        for i in range(n):
            dfs(i)
        return res

            
            