class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = {}
        def sol(try_from, i):
            if (try_from, i) not in dp:
                ci = i
                for j in range(try_from, len(s)):
                    if s[ci:j+1] in d:
                        if sol(j + 1, ci):
                            dp[(try_from,i)] = True
                            break
                        ci = j+1
                    if j - ci + 1 >= len(s):
                        dp[(try_from,i)] = False
                        break
                if (try_from,i) not in dp:
                    dp[(try_from,i)] = len(s) == ci
            return dp[(try_from,i)]
        return sol(0, 0)