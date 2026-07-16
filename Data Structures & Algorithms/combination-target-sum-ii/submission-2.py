class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        cur = []
        slotted = defaultdict(set)
        nums.sort()
        def dfs(start, tot):
            if tot == target:
                sol.append([*cur])
            elif tot < target:
                l = len(cur)
                for i in range(start,len(nums)):
                    if nums[i] not in slotted[l]:
                        slotted[l].add(nums[i])
                        cur.append(nums[i])
                        dfs(i + 1, tot + nums[i])
                        cur.pop()
                slotted[l] = set()
        dfs(0, 0)
        return sol
