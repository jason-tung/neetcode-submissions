# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def sol(root):
            if not res[0]:
                return 0
            if not root:
                return 0
            l,r = sol(root.left), sol(root.right)
            if abs(l - r) > 1:
                res[0] = False
            return 1 + max(l,r)
        sol(root)
        return res[0]
            
