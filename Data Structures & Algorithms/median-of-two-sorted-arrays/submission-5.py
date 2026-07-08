class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def take(a, i):
            if i < 0:
                return float("-inf")
            if i >= len(a):
                return float("inf")
            return a[i]

        A, B = nums2, nums1
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        n, m = len(A), len(B)
        left_total = (n + m) // 2
        lo, hi = 0, n
        while True:
            i = (lo + hi) // 2
            j = left_total - i
            left_a, right_a = take(A, i - 1), take(A, i)
            left_b, right_b = take(B, j - 1), take(B, j)
            if left_a <= right_b and left_b <= right_a:
                if (n + m) % 2:
                    return min(right_b, right_a)
                return (max(left_a, left_b) + min(right_b, right_a)) / 2.0
            if left_a > right_b:
                hi = i - 1
            else:
                lo = i + 1
