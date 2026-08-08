class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom up lazy cache no optimization
        # dp[i] = dp[i-1] + dp[i-2] if s[i-1] + s[i] is valid
        # if s[i] is 0 -> always take dp[i-2] because dp[i-1] treats s[i] as a valid 1 character when it must actually be a part of a two char sequence.
        dp = [-1] * len(s)
        prev = 0
        def sol(i):
            if i < 0:
                return 1
            if dp[i] == -1:
                # 0 needs to be paired with an appropriate prev
                # 0 now means prev overcounted - correct by taking sol[i-2]
                if s[i] == "0":
                    if prev != 1 and prev != 2:
                        dp[i] = 0
                    else:
                        dp[i] = sol(i-2)
                else:
                    # try to make a "branch" by interpretting prev + cur as "1" "2" or "12" 
                    if prev == 1 or prev == 2 and int(s[i]) <= 6:
                        dp[i] = sol(i-1) + sol(i-2)
                    else:
                        dp[i] = sol(i-1)
            return dp[i]
        for k in range(len(s)):
            sol(k)
            prev = int(s[k])
        return dp[-1]