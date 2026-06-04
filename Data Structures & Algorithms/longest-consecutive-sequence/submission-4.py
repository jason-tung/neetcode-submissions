class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        r = 0
        for k in nums:
            if seen[k] == 0:
                seen[k] = seen[k-1] + seen[k+1] + 1
                seen[k-seen[k-1]] = seen[k]
                seen[k+seen[k+1]] = seen[k]
            r = max(seen[k], r)
        return r

