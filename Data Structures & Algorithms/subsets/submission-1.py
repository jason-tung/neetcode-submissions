class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        def helper(i, cur):
            if i < len(nums):
                n = [nums[i], *cur]
                sol.append(n)
                if i+1 < len(nums):
                    helper(i+1, cur)
                    helper(i+1, n)
        helper(0, [])
        return sol
            
            