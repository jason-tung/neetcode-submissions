class Solution:
    def part(self, a,lo,hi):
            i,j = lo-1, hi + 1
            m = a[(i + j)//2]
            while True:
                i += 1
                j -= 1
                while i <= j and a[i] > m:
                    i += 1
                while i <= j and a[j] < m:
                    j -= 1
                if i >= j:
                    return j
                a[i],a[j] = a[j],a[i]
    def qselect(self, a, lo, hi, k):
        if lo < hi:
            p = self.part(a, lo, hi)
            if p < k:
                return self.qselect(a, p + 1, hi, k)
            else:
                return self.qselect(a, lo, p, k)
        return a[hi]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qselect(nums, 0, len(nums) - 1, k - 1)

        
        