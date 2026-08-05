class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = deque([s[0]])
        def solve(cur, l, r):
            nonlocal sol
            for incr in range(min(l, len(s) - 1 - r)):
                incr += 1
                lc,rc = s[l-incr],s[r+incr]
                if lc == rc:
                    cur.appendleft(lc)
                    cur.append(rc)
                else:
                    break
            if len(cur) >= len(sol):
                sol = deque(cur)
        for i in range(len(s)):
            solve(deque([s[i]]), i, i)
            if i != len(s) - 1 and s[i] == s[i+1]:
                solve(deque([s[i], s[i+1]]), i, i+1)
        return "".join(sol)
