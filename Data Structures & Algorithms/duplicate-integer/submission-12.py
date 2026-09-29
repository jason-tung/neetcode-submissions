class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for k in nums:
            if k in s:
                return True
            s.add(k)
        return False