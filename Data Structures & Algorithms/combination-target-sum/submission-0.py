class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        cur = []
        def dfs(start, tot):
            if tot == target:
                sol.append([*cur])
            elif tot < target:
                for i in range(start,len(nums)):
                    cur.append(nums[i])
                    dfs(i, tot + nums[i])
                    cur.pop()
        dfs(0, 0)
        return sol

