class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len, index = 0, 0
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    if length > max_len:
                        max_len = length
                        index = i
        return s[index:index+max_len]
                    
