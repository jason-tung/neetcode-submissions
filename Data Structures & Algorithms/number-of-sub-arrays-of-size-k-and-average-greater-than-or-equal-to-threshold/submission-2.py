class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        goal = k * threshold
        s = 0
        res = 0
        for r in range(len(arr)):
            s += arr[r]
            if r >= k:
                s -= arr[r-k]
            if r >= k - 1 and s >= goal:
                res += 1
        return res