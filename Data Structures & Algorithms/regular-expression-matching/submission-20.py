class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        dp = [False] * (n+1)
        for i in range(m, -1, -1):
            nxt = [False] * (n + 1)
            for j in range(n, -1, -1):
                if i == m:
                    if j == n:
                        nxt[j] = True
                    elif j + 1 < n and p[j + 1] == "*":
                        nxt[j] = nxt[j+2]
                elif j != n:
                    is_match = s[i] == p[j] or p[j] == "."
                    if j + 1 < n and p[j+1] == "*":
                        nxt[j] = nxt[j+2]
                        if is_match:
                            nxt[j] |= dp[j]
                    elif is_match:
                        nxt[j] = dp[j+1]
                    else:
                        nxt[j] = False
            dp = nxt
        return dp[0]
                        