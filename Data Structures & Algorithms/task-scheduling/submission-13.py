class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        m = max(d.values())
        most_freq_count = sum(1 if d[k] == m else 0 for k in d)
        return max((m - 1) * (n + 1) + most_freq_count, len(tasks))