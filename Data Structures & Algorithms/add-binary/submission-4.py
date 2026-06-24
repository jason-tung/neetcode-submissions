class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = deque()
        co = 0
        for i in range(1,max(len(a),len(b))+1):
            ad = bd = 0
            if i <= len(a):
                ad = int(a[-i])
            if i <= len(b):
                bd = int(b[-i])
            local_sum = ad + bd + co
            co = local_sum >> 1
            dig = local_sum & 1
            res.appendleft(dig)
        if co:
            res.appendleft(co)
        return ''.join(str(k) for k in res)
                