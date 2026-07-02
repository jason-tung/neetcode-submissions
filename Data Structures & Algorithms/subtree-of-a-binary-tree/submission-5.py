# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def serialize(root):
            res = []
            def helper(root):
                if not root:
                    res.append("#")
                    return
                res.append(str(root.val))
                helper(root.left)
                helper(root.right)
            helper(root)
            return '^'.join(res)
        root_serial = serialize(root)
        subroot_serial = serialize(subroot)
        return subroot_serial in root_serial
            
