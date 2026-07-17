class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        cur = []
        nums.sort()
        def dfs(start, tot):
            if tot == target:
                sol.append([*cur])
            elif tot < target:
                slotted = set()
                for i in range(start,len(nums)):
                    if nums[i] not in slotted:
                        slotted.add(nums[i])
                        cur.append(nums[i])
                        dfs(i + 1, tot + nums[i])
                        cur.pop()
        dfs(0, 0)
        return sol
