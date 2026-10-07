class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        m = max(d.values())
        num_m = sum(1 for k in d if d[k] == m)
        min_sizing = (n + 1) * (m - 1) + num_m
        return max(min_sizing, len(tasks))