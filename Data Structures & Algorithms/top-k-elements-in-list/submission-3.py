class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n,f in freq.items():
            buckets[f].append(n)
        ret = []
        pointer = -1
        while len(ret) < k:
            while pointer >= -len(buckets) and len(buckets) == 0:
                pointer -= 1
            ret.extend(n for n in buckets[pointer])
            pointer -= 1
        return ret
        
