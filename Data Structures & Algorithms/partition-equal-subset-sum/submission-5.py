class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        s = set([0])
        for n in nums:
            sprime = set()
            for t in s:
                if n + t == target:
                    return True
                if n + t < target:
                    sprime.add(n + t)
                sprime.add(t)
            s = sprime
        return False
        
            
