class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        co = 0
        for i in range(1,max(len(a),len(b))+1):
            ad = bd = 0
            if i <= len(a):
                ad = int(a[-i])
            if i <= len(b):
                bd = int(b[-i])
            local_sum = ad + bd + co
            print(ad, bd, co, local_sum)
            co = local_sum >> 1
            dig = local_sum & 1
            res.append(str(dig))
        if co:
            res.append(str(co))
        return ''.join(res[::-1])
                