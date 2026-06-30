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
        prev = ret = None
        o2n = {}
        while head:
            n = Node(head.val)
            if not ret:
                ret = n
            n.random = head.random
            o2n[head] = n
            if prev:
                prev.next = n
            prev = n
            head = head.next
        tmp = ret
        while tmp:
            if tmp.random:
                tmp.random = o2n[tmp.random]
            tmp = tmp.next
        return ret

            