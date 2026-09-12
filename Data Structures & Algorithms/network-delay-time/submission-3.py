class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)
        done = set()
        for u,v,t in times:
            d[u].append((t,v))
        q = [(0,k)]
        cost = 0
        while q and len(done) != n:
            pu, u = heapq.heappop(q)
            if u in done:
                continue
            done.add(u)
            cost = max(pu, cost)
            for (pv, v) in d[u]:
                if v not in done:
                    pt = pv + pu
                    heapq.heappush(q, (pt, v))
        return cost if len(done) == n else -1
        
    
# node -> (price, output)

# pop top of minhead
# for each d[u]
# enqueue onto minheap as (total price, outputnode)