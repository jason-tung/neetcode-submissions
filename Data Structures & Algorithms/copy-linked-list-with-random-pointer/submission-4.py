"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        o2n = {}
        def helper(node):
            if not node:
                return
            n = Node(node.val)
            o2n[node] = n
            helper(node.next)
        def helper2(node):
            if not node:
                return
            n = o2n[node]
            n.next = o2n[node.next] if node.next else None
            n.random = o2n[node.random] if node.random else None
            helper2(node.next)
        helper(head)
        helper2(head)
        return o2n[head] if head else None
                

            