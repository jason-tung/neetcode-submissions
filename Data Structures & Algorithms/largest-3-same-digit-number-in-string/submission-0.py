class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = '-1'
        l,r = 0, 0
        while r < len(num):
            if num[l] != num[r]:
                    l = r
            if r - l + 1 > 3:
                l+=1
            if r - l + 1 == 3 and int(num[l]) > int(m):
                m = num[l]
            r += 1
        return m * 3 if m != '-1' else ''