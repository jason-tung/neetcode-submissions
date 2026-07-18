class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        cur = []
        used = set()
        def dfs (i,j):
            has_ans = False
            if 0 <= i < rows and 0 <= j < cols:
                if board[i][j] == word[len(cur)] and (i,j) not in used:
                    cur.append(board[i][j])
                    if len(cur) == len(word):
                        return True
                    used.add((i,j))
                    for (a,b) in [(0,1),(0,-1),(1,0), (-1,0)]:
                        has_ans = has_ans or dfs(i+a, j+b)
                    cur.pop()
                    used.remove((i,j))
            return has_ans
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j):
                    return True
        return False
