class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        for k in nums:
            if seen[k] == 0:
                seen[k] = seen[k-1] + seen[k+1] + 1
                seen[k-seen[k-1]] = seen[k]
                seen[k+seen[k+1]] = seen[k]
        return max(seen.values()) if len(seen) else 0

