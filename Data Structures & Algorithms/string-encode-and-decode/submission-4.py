class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for x in strs:
            s+=f'{len(x)}#{x}'
        return s
    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            word_len = int(s[i:j])
            r.append(s[j+1:j+ word_len + 1])
            i = j + word_len + 1
        return r

            
            