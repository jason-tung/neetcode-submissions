# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def helper(node):
            nonlocal res
            if not node:
                res.append("_")
            else:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
        helper(root)
        return ','.join(res)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        i = 0
        def helper():
            nonlocal i
            if data[i] == '_':
                i += 1
                return None
            ret = TreeNode(data[i])
            i += 1
            ret.left = helper()
            ret.right = helper()
            return ret
        return helper()


            
