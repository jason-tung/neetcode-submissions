class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        sol = []
        def dfs(l_left, need_r):
            if not l_left and not need_r:
                sol.append(''.join(cur))
            if l_left:
                cur.append('(')
                dfs(l_left - 1, need_r + 1)
                cur.pop()
            if need_r:
                cur.append(')')
                dfs(l_left, need_r - 1)
                cur.pop()
        dfs(n,0)
        return sol