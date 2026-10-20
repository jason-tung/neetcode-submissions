class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            rep = []
            for i in range(26):
                if counter[i]:
                    rep.append(str(i))
                    rep.append(str(counter[i]))
            res[','.join(rep)].append(s)
        return list(res.values())