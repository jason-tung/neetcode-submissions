# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def dfs(node, level):
            nonlocal levels
            if node:
                levels[level].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        dfs(root, 0)
        res = [[] for k in levels]
        for k in levels:
            res[k] = levels[k]
        return res