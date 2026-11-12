class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new = []
            for r in res:
                new.append(r + [num])
            res.extend(new)
        return res