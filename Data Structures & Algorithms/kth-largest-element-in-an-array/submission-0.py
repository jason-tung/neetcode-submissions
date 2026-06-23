class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1
        l,r = 0, len(nums) - 1
        while l < r:
            p = self.part(nums, l, r)
            if k <= p:
                r = p
            else:
                l = p + 1
        return nums[r]
        
    def part(self, a, l, r):
        i, j = l - 1, r + 1
        pivot = a[(l + r)//2]
        while True:
            i += 1
            j -= 1
            while a[i] > pivot:
                i += 1
            while a[j] < pivot:
                j -= 1
            if j <= i:
                return j
            a[i], a[j] = a[j], a[i]
        
        