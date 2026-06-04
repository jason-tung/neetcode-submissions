class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        nums.sort()
        for k in nums:
            seen[k] = seen[k-1] + 1
        return max(seen.values()) if len(seen) else 0

