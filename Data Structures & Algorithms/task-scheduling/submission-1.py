class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        h = list((v, k) for (k,v) in Counter(tasks).items())
        heapq.heapify_max(h)
        q = deque()
        while h or q:
            while q and q[0][0] <= time:
                candidate = q.popleft()
                heapq.heappush_max(h, (candidate[1], candidate[2]))
            if h:
                (freq, key) = heapq.heappop_max(h)
                if freq > 1:
                    q.append((time + n + 1, freq - 1, key))
            time += 1
        return time



