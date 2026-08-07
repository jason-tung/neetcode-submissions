class Solution:
    def numDecodings(self, s: str) -> int:
# opt(i) = opt(i-1) + opt(i-2) if s[i-1] + s[i] is valid
        sol_1, sol_2 = 1, 1
        prev = -1
        for k in s:
            k = int(k)
            if k == 0:
                if prev != 1 and prev != 2:
                    return 0
                # if we use 0 then we can't use prev as 2 digit combo
                sol_2 = sol_1
            else:
                tmp = sol_2 
                # if we can interpret current as 2 digit combo using prev
                if prev == 1 or prev == 2 and k <= 6:
                    sol_2 = sol_2 + sol_1
                sol_1 = tmp
            prev = k
        return sol_2