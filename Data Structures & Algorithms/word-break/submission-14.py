class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = dict((k, True) for k in wordDict)
        dp = [-1] * (len(s) + 1)
        dp[-1] = 1
        def sol(i):
            if i > len(s):
                return False
            if dp[i] == -1:
                dp[i] = 0
                for k in d:
                    if s[i:i+len(k)] == k:
                        if sol(i+len(k)):
                            dp[i] = 1
            return dp[i]
        return sol(0) == 1