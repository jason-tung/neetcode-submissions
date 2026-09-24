class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp=[False] * (m+1)
        for i in range(n, -1, -1):
            nxt_row = dp.copy()
            for j in range(m, -1, -1):
                if j == m:
                    nxt_row[j] = i == n
                    continue
                cur_match = i < n and (s[i] == p[j] or p[j] == ".")
                if j + 1 < m and p[j + 1] == "*":
                    if cur_match:
                        nxt_row[j] = dp[j] or nxt_row[j+2]
                    else:
                        nxt_row[j] = nxt_row[j+2]
                elif cur_match:
                    nxt_row[j] = dp[j+1]
                else:
                    nxt_row[j] = False 
            dp = nxt_row
        return dp[0]