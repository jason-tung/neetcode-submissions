class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        for k in nums:
            sol.extend([[k,*cur] for cur in sol])
        return sol