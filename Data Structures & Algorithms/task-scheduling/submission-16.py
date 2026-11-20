class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        num_windows = max(d.values())
        num_freq_task = sum(1 for k in d if d[k] == num_windows)
        return max(len(tasks), (n + 1) * (num_windows - 1) + num_freq_task)