class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        visited = set()
        def dfs():
            if len(cur) == len(nums):
                res.append([*cur])
                return
            for k in nums:
                if k not in visited:
                    visited.add(k)
                    cur.append(k)
                    dfs()
                    visited.remove(k)
                    cur.pop()
        dfs()
        return res