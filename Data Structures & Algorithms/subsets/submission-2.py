class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        cur = []
        def helper(i):
            if i >= len(nums):
                sol.append([*cur])
            else:
                cur.append(nums[i])
                helper(i+1)
                cur.pop()
                helper(i+1)
        helper(0)
        return sol
        