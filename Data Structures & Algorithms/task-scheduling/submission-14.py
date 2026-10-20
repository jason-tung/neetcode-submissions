class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        max_freq = max(d.values())
        num_max_freq = sum(1 if d[k] == max_freq else 0 for k in d)
        return max(len(tasks), (n + 1) * (max_freq - 1) + num_max_freq)