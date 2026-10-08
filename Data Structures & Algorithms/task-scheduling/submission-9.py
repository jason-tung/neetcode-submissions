import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        d = Counter(tasks)
        h = [(freq, job) for job, freq in d.items()]
        heapq.heapify_max(h)
        q = deque()
        while h or q:
            if h:
                freq, job = heapq.heappop_max(h)
                freq -= 1
                time += 1
                if freq > 0:
                    q.append((time + n,freq, job))
            else:
                time = q[0][0]
            while q and q[0][0] <= time:
                _, freq, job = q.popleft()
                heapq.heappush_max(h, (freq, job))
        return time