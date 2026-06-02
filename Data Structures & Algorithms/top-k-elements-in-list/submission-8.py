class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freq_l = [(-freq, ele) for (ele, freq) in freqs.items()]
        # top k elements 
        return self.quickselect(freq_l, 0, len(freq_l)-1, k-1)

    def quickselect(self, nums, l, r, k):
        if l == r:
            return [x[1] for x in nums[:k+1]]
        m = self.part(nums, l, r)
        if k <= m:
            return self.quickselect(nums, l, m, k)
        else:
            return self.quickselect(nums, m+1, r, k)
        
    def part(self, nums, l, r):
        li, ri = l-1, r+1
        piv = nums[(l + r) // 2][0]
        while True:
            li += 1
            ri -= 1
            while nums[li][0] < piv:
                li += 1
            while nums[ri][0] > piv:
                ri -= 1
            if li >= ri:
                return ri
            nums[ri], nums[li] = nums[li], nums[ri]
