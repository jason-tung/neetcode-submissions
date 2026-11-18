# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        res = head = ListNode()
        i = len(lists)
        while heap:
            _, _, l = heapq.heappop(heap)
            head.next = l
            head = head.next
            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))
                i += 1
        return res.next