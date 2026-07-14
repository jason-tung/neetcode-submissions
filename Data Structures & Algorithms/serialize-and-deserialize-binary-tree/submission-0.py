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
        dummy = head = TreeNode()
        data = data.split(',')
        print(data)
        def helper(data, i):
            if i < len(data):
                if data[i] == '_':
                    return (None, 1)
                ret = TreeNode(int(data[i]))
                l=helper(data,i+1)
                r=helper(data,i+l[1]+1)
                ret.left=l[0]
                ret.right=r[0]
                return (ret, 1 + l[1] + r[1])
        return helper(data, 0)[0]


            
