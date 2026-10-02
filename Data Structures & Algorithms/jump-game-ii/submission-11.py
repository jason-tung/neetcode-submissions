class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        q = deque([(0, 0)])
        visited = set([0])
        while q:
            i, cost = q.popleft()
            for k in range(nums[i]):
                j = i + k + 1
                if j == n - 1:
                    return cost + 1
                if j not in visited:
                    visited.add(j)
                    q.append((j, cost + 1))
