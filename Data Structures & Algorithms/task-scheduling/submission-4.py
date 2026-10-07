import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        heap = [(-v, k) for k,v in d.items()]
        q = deque()
        heapq.heapify(heap)
        t = 0
        while heap or q:
            if heap:
                freq, c = heapq.heappop(heap)
                t += 1
                if freq + 1 < 0:
                    q.append((t + n, freq + 1, c))
            else:
                tmp = t
                t = q[0][0]
            while q and q[0][0] <= t:
                _,freq,c = q.popleft()
                heapq.heappush(heap, (freq, c))
        return t

        
                