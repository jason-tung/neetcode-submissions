# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a,b = min(p.val,q.val), max(p.val,q.val)
        while root:
            if root.val >= a and root.val <= b:
                return root
            elif root.val > b:
                root = root.left
            else:
                root = root.right
        return None