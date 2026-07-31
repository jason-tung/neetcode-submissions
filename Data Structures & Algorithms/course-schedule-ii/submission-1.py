class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = [[] for _ in range(numCourses)]
        ind = [0]*numCourses
        for (a,b) in prerequisites:
            d[b].append(a)
            ind[a] += 1
        q = deque([k for k in range(numCourses) if ind[k] == 0])
        solved = []
        while q:
            n = q.popleft()
            solved.append(n)
            for k in d[n]:
                ind[k] -= 1
                if not ind[k]:
                    q.append(k)
        return solved if len(solved) == numCourses else []