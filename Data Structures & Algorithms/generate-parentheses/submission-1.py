class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(open_remain,close_remain):
            if not open_remain and not close_remain:
                res.append(''.join(cur))
            if open_remain:
                cur.append("(")
                dfs(open_remain-1, close_remain+1)
                cur.pop()
            if close_remain:
                cur.append(")")
                dfs(open_remain, close_remain-1)
                cur.pop()
        dfs(n,0)
        return res
                
