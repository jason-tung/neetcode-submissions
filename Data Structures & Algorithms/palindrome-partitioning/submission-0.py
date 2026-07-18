class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        cur_partition = []
        working_substr = []
        def dfs(i):
            nonlocal working_substr
            if i == len(s):
                if not working_substr:
                    sol.append([*cur_partition])
            else:
                working_substr.append(s[i])
                if working_substr == working_substr[::-1]:
                    tmp = working_substr
                    cur_partition.append(''.join(working_substr))
                    working_substr = []
                    dfs(i+1)
                    cur_partition.pop()
                    working_substr = tmp
                dfs(i+1)         
                working_substr.pop()
        dfs(0)
        return sol
                    
