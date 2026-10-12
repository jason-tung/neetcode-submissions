class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        h = [(-v,k) for k,v in d.items()]
        q = deque()
        heapq.heapify(h)
        time = 0
        while h or q:
            time += 1

            if h:
                freq, k = heapq.heappop(h)
                freq += 1
                if freq != 0:
                    q.append((time + n, freq, k))

            if q and q[0][0] <= time:
                _,freq,k = q.popleft()
                heapq.heappush(h, (freq, k))
        return time