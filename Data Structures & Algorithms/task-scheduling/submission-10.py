class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        m = max(d.values())
        num_max = sum(1 if d[k] == m else 0 for k in d)
        return max((n + 1) * (m - 1) + num_max, len(tasks))