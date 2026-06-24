class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(0,0)])
        # visited vs min to get to
        visited = {}
        while queue:
            (i, dis) = queue.pop()
            if i not in visited or i in visited and visited[i] > dis:
                visited[i] = dis
                for j in range(i, i + nums[i] + 1):
                    if j <= len(nums) - 1:
                        queue.append((j, dis + 1))
        return visited[len(nums) - 1]