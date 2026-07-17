class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        cur = []
        nums.sort()
        def dfs(i):
            sol.append([*cur])
            if len(cur) == len(nums):
                return
            s = set()
            for idx in range(i, len(nums)):
                k = nums[idx]
                if k not in s:
                    s.add(k)
                    cur.append(k)
                    dfs(idx+1)
                    cur.pop()
        dfs(0)
        return sol