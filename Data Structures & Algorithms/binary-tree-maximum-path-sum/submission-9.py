# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-math.inf]
        def sol(root):
            if not root:
                return 0
            left = max(0, sol(root.left))
            right = max(0, sol(root.right))
            res[0] = max(res[0], left + right + root.val)
            return max(left + root.val, right + root.val)
        sol(root)
        return res[0]