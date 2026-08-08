class Solution:
    def numDecodings(self, s: str) -> int:
        # top down
        dp = [-1] * len(s)
        def sol(i):
            if i < 0:
                return 1
            if dp[i] == -1:
                prev = int(s[i - 1]) if i > 0 else 0
                if s[i] == "0":
                    if prev != 1 and prev != 2:
                        dp[i] = 0
                    else:
                        dp[i] = sol(i-2)
                else:
                    if prev == 1 or prev == 2 and int(s[i]) <= 6:
                        dp[i] = sol(i-1) + sol(i-2)
                    else:
                        dp[i] = sol(i-1)
            return dp[i]
        return sol(len(s) - 1)