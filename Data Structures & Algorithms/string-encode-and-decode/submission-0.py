class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for x in range(len(strs)):
            s+=f'{len(strs[x])}#{strs[x]}'
        return s+"."
    def decode(self, s: str) -> List[str]:
        r = []
        mode = 0
        l = -1
        cur = ""
        for x in s:
            if l == 0:
                r.append(cur)
                cur = ""
                mode = 0
                l = -1
            if mode == 0:
                if x != "#":
                    cur += x
                else:
                    l = int(cur)
                    cur = ""
                    mode = 1
            else:
                cur += x
                l -= 1
        return r

            
            