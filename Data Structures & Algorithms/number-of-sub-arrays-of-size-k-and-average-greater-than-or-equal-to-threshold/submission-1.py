class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        goal = k * threshold
        l,r = 0, -1
        s = 0
        res = 0
        while r < len(arr) - 1:
            r += 1
            s += arr[r]
            while r - l + 1 < k:
                r += 1
                s += arr[r]
            while r - l + 1 > k:
                s -= arr[l]
                l += 1
            if s >= goal:
                res += 1
        return res