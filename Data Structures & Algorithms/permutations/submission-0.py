class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        cur = []
        cur_set = set()
        def dfs():
            if len(cur) == len(nums):
                return sol.append([*cur])
            for k in nums:
                if k not in cur_set:
                    cur.append(k)
                    cur_set.add(k)
                    dfs()
                    cur.pop()
                    cur_set.remove(k)
        dfs()
        return sol
