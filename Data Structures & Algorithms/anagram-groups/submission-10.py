class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            t = [0] * 26
            for c in s:
                t[ord(c) - ord('a')] += 1
            d[tuple(t)].append(s)
        return list(d.values())