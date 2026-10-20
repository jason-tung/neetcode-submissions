class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            rep = []
            d = Counter(s)
            for c in sorted(d.keys()):
                rep.append(c)
                rep.append(str(d[c]))
            res[''.join(rep)].append(s)
        return list(res.values())