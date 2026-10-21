class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[(m-1)%n]:
                l = m
                break
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        r = l + n - 1
        while l <= r:
            m = (l + r) // 2
            mn = m % n
            if nums[mn] == target:
                return mn
            elif nums[mn] < target:
                l = m + 1
            else:
                r = m -1
        return -1