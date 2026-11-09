# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[-math.inf]
        def sol(node):
            if not node:
                return 0
            l = max(0, sol(node.left))
            r = max(0, sol(node.right))
            res[0] = max(res[0], node.val + l + r)
            return node.val + max(l, r)
        sol(root)
        return res[0]