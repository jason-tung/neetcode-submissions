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
        head_store = head
        while head:
            n = Node(head.val)
            o2n[head] = n
            head = head.next
        head = head_store
        while head:
            n = o2n[head]
            if head.random:
                n.random = o2n[head.random]
            if head.next:
                n.next = o2n[head.next]
            head = head.next
        return o2n[head_store] if head_store else None

            