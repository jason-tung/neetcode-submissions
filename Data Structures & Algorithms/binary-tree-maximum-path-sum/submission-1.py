# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = float('-inf')
        def sol(node):
            if not node:
                return 0
            l,r = sol(node.left), sol(node.right)
            bw = node.val + l + r
            lr = node.val + max(l,r , 0)
            nonlocal m
            m = max(m, lr, bw)
            return lr
        sol(root)
        return m