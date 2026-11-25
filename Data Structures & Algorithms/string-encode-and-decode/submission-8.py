class Solution:

    def encode(self, strs: List[str]) -> str:
        tokens = []
        for s in strs:
            tokens.append(str(len(s)))
            tokens.append("@")
            tokens.append(s)
        return ''.join(tokens)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        r, l, ln = 0, 0, -1
        cur = []
        while r < len(s) or ln != -1:
            if ln == -1:
                if s[r] != '@':
                    cur.append(s[r])
                else:
                    ln = int(''.join(cur))
                    l = r + 1
                    cur = []
            elif ln != 0:
                cur.append(s[r])
                if r >= l + ln - 1:
                    ln = -1
                    res.append(''.join(cur))
                    cur = []
            if ln == 0:
                ln = -1
                res.append(''.join(cur))
                cur = []
            r += 1
        return res
                