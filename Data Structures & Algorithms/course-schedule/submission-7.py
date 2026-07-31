class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {}
        ind = defaultdict(int)
        q = set(range(numCourses))
        for k in range(numCourses):
            d[k] = set()
        for (a,b) in prerequisites:
            d[b].add(a)
            ind[a] += 1
            q.discard(a)
        q = deque(q)
        solved = set()
        while q:
            n = q.popleft()
            solved.add(n)
            for k in d[n]:
                if k in solved:
                    return False
                ind[k] -= 1
                if not ind[k]:
                    q.append(k)
        return len(solved) == numCourses