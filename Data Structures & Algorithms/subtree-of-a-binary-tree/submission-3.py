# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return not subroot
        def helper(root, subroot):
            if not root or not subroot:
                return not subroot and not root
            if root.val != subroot.val:
                return False
            return helper(root.left, subroot.left) and helper(root.right, subroot.right)
        return helper(root, subroot) or self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
