class Solution:
    def generate_map(self):
        d = defaultdict(set)
        i = 0
        for k in range(2,10):
            for _ in range(3):
                d[str(k)].add(chr(ord('a') + i))
                i += 1
            if k == 7 or k == 9:
                d[str(k)].add(chr(ord('a') + i))
                i += 1
        return d
    def letterCombinations(self, digits: str) -> List[str]:
        ltr_map = self.generate_map()
        sol = []
        cur = []
        def dfs(i):
            if i == len(digits):
                if cur: 
                    sol.append(''.join(cur))
                return
            for ltr in ltr_map[digits[i]]:
                cur.append(ltr)
                dfs(i+1)
                cur.pop()
        dfs(0)
        return sol
                
        