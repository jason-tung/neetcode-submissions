class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tupes = [0] * 26
            for c in s:
                tupes[ord(c) - ord('a')] += 1
            res[tuple(tupes)].append(s)
        return list(res.values())