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
        ln = -1
        cur = []
        for r in range(len(s)):
            if ln == -1:
                if s[r] == "@":
                    ln = int(''.join(cur))
                    cur = []
                    if ln == 0:
                        res.append('')
                        ln = -1
                else:
                    cur.append(s[r])
            else:
                cur.append(s[r])
                ln -= 1
                if ln == 0:
                    res.append(''.join(cur))
                    cur = []
                    ln = -1
        return res
                