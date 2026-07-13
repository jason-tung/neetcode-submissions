# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        head = dummy
        def debug(node):
            s = ""
            i = 0
            while node:
                i += 1
                if i > 10:
                    return s+"inf"
                s += str(node.val)+","
                node = node.next
            return s
        def reverse(prev_node, cur, stopper):
            last_after_reverse = cur
            prev_node.next = stopper
            prev = stopper.next
            while True:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                if prev == stopper:
                    return last_after_reverse
        def skip(node, k):
            while k:
                if not node:
                    return None
                node = node.next
                k -= 1
            return node
        while True:
            # print("head",head.val)
            # print("debug", debug(dummy))
            stopper = skip(head, k)
            # print("stopper", stopper.val if stopper else None)
            if not stopper:
                print("stopper")
                return dummy.next
            head = reverse(head, head.next, stopper)            
            

            
                
        
            
            