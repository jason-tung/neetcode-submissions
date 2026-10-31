# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = res = ListNode()
        pq = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(pq)
        i = len(lists)
        while pq:
            _, _, l = heapq.heappop(pq)
            head.next = head = l
            if l.next:
                heapq.heappush(pq, (l.next.val, i, l.next))
                i += 1
        return res.next