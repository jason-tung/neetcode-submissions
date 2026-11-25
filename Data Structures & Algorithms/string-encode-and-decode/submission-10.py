class Solution:

    def encode(self, strs: List[str]) -> str:
        tokens = []
        for s in strs:
            tokens.append(str(len(s)))
            tokens.append("@")
            tokens.append(s)
        return ''.join(tokens)

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0
        while r < len(s):
            if s[r] == '@':
                ln = int(s[l:r])
                r += 1
                res.append(s[r:r+ln])
                r += ln
                l = r
            else:
                r += 1
        return res
                
        # 3@abc3@xyz
        # 0123456789