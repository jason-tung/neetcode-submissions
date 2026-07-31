class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = [[] for _ in range(numCourses)]
        ind = [0]*numCourses
        
        for (a,b) in prerequisites:
            d[b].append(a)
            ind[a] += 1
        q = deque([k for k in range(numCourses) if ind[k] == 0])
        solved = 0
        while q:
            n = q.popleft()
            solved += 1
            for k in d[n]:
                ind[k] -= 1
                if not ind[k]:
                    q.append(k)
        return solved == numCourses