class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def take(a, i):
            if i < 0:
                return float('-inf')
            if i >= len(a):
                return float('inf')
            return a[i]
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        total_size = len(A) + len(B)
        left_total = total_size//2
        lo, hi = 0, len(A)
        i = 0
        while lo <= hi:
            i += 1
            if i > 10:
                return
            a_left_size = (lo + hi)//2
            b_left_size = left_total - a_left_size
            left_a, right_b = take(A, a_left_size - 1), take(B, b_left_size)
            # left cut of a too big
            # print(f'taking {a_left_size} from A {b_left_size} from B')
            # print("+", left_a, right_b)
            if left_a > right_b:
                hi = a_left_size - 1
            else:
                # if left_a bigger than left_b we are good
                left_b = take(B, b_left_size - 1)
                right_a = take(A, a_left_size)
                if left_a >= left_b:
                    lo = hi = a_left_size
                    break
                lo = a_left_size + 1
        right_min = min(take(A, hi), take(B, left_total - hi))
        if total_size % 2:
            return right_min
        return (max(take(A, hi - 1), take(B, left_total - hi - 1)) + right_min) / 2.0

        
