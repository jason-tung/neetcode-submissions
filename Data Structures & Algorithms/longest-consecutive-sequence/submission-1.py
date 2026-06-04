class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        m = 0
        for k in nums:
            if k-1 not in seen:
                i = 0
                while k + i in seen:
                    i += 1
                m = max(m,i)
        return m

