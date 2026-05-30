class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n,f in freq.items():
            buckets[f].append(n)
        return [num for bucket in buckets for num in bucket][-k:]
        
