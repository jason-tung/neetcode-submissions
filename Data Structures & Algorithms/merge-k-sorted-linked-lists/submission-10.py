# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        i = len(lists)
        pq = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(pq)
        while pq:
            _, _, l = heapq.heappop(pq)
            node.next = l
            node = l
            if l.next:
                heapq.heappush(pq, (l.next.val, i, l.next))
                i += 1
        return dummy.next