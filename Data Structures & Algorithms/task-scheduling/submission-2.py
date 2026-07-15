class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        vals = [v for v in Counter(tasks).values()]
        m = max(vals)
        c = sum(1 if v == m else 0 for v in vals)
        return max(len(tasks), (m-1) * (n+1) + c)