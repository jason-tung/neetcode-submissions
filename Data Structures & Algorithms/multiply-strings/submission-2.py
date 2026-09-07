class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(a1, a2, size):
            co = 0
            res = [0] * size
            for i in range(size - 1, -1, -1):
                s = co
                s += a1[i]
                s += a2[i]
                res[i] = s%10
                co = s // 10
            return res
        nm = len(num1) + len(num2) + 1
        res = [0] * nm
        for i in range(len(num2)):
            prod = [0] * nm
            idx = len(num2) - 1 - i
            co = 0
            for j in range(len(num1)):
                jdx = len(num1) - 1 - j
                s = co + int(num2[idx]) * int(num1[jdx])
                prod[nm - 1 - i - j] = s % 10
                co = s // 10
            prod[nm - 1 - len(num1) - i] = co
            res = add(res, prod, nm)
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return ''.join([str(k) for k in res[i:]]) if i < nm else "0"

            

            