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
        d = {}
        def get(node):
            if not node:
                return None
            if node not in d:
                d[node] = Node(node.val)
            return d[node]
        l1 = head
        while l1:
            l2 = get(l1)
            l2.next = get(l1.next)
            l2.random = get(l1.random)
            l1 = l1.next 
        return get(head)