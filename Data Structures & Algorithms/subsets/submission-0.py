class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        def helper(nums, i, cur):
            if i < len(nums):
                n = [nums[i], *cur]
                sol.append(n)
                if i+1 < len(nums):
                    helper(nums, i+1, cur)
                    helper(nums, i+1, n)
        helper(nums, 0, [])
        return sol
            
            