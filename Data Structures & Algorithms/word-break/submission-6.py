class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = [-1] * len(s)
        def sol(i):
            if i >= len(s):
                return
            if dp[i] == -1:
                for k in d:
                    if s[i:i+len(k)] == k:
                        dp[i+len(k)-1] = True
                        sol(i+len(k))
            return dp[-1]
        return sol(0) != -1