# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            res = dummy = ListNode()
            while l1 or l2:
                if not l2 or l1 and l1.val <= l2.val:
                    n = l1
                    l1 = l1.next
                elif not l1 or l2 and l2.val <= l1.val:
                    n = l2
                    l2 = l2.next
                res.next = n
                res = res.next
                n.next = None
            return dummy.next
        while len(lists) > 1:
            tmp = []
            for i in range(0,len(lists),2):
                j = i + 1
                if j < len(lists):
                    tmp.append(merge(lists[i], lists[j]))
                else:
                    tmp.append(lists[i])
            lists = tmp
        return lists[0] if lists else None
        
            
                