class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = [int(k) for k in num1], [int(k) for k in num2]
        n, m = len(num1), len(num2)
        res = [0] * (n + m)
        for i in range(n):
            for j in range(m):
                i_rev, j_rev = n - 1 - i, m - 1 - j
                res[n + m - 1 - i - j] +=  num1[i_rev] * num2[j_rev]
        i = n + m - 1
        co = 0
        while i >= 0:
            s = co + res[i]
            res[i] = s % 10
            co = s // 10
            i -= 1
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1
        res = [str(k) for k in res[i:]]
        return ''.join(res)
        