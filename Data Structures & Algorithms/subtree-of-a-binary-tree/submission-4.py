# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        res = []
        def serialize(root):
            if not root:
                res.append("^#")
                return
            res.append(f'^{str(root.val)}')
            serialize(root.left)
            serialize(root.right)
        serialize(root)
        root_serial = ''.join(res)
        res = []
        serialize(subroot)
        subroot_serial = ''.join(res)
        return subroot_serial in root_serial
            
