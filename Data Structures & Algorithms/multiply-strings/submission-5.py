class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(a, i,co):
            while co:
                s = (int(a[i]) if a[i] else 0) + co
                a[i] = str(s % 10)
                co = s // 10
                i -= 1
        n, m = len(num1), len(num2)
        res = ['0'] * (n + m)
        for i in range(n):
            for j in range(m):
                i_rev, j_rev = n - 1 - i, m - 1 - j
                add(res, n + m - 1 - i - j, int(num1[i_rev]) * int(num2[j_rev]))
        i = 0
        while i < len(res) - 1 and res[i] == '0':
            i += 1
        return ''.join(res[i:])
        