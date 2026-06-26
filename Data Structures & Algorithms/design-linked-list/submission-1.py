class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt
        
    def __str__(self):
        s = ""
        t = self
        while t:
            s += str(t.val) + ","
            t = t.next
        return s

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        t = self.head
        for _ in range(index):
            t = t.next if t and t.next else None
        return t.val if t else -1

    def addAtHead(self, val: int) -> None:
        n = Node(val, self.head)
        self.head = n
        if not self.tail:
            self.tail = n

    def addAtTail(self, val: int) -> None:
        n = Node(val)
        if self.tail:
            self.tail.next = n
        self.tail = n
        if not self.head:
            self.head = n

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        prev, now = None, self.head
        for _ in range(index):
            prev = now
            now = now.next if now and now.next else None
        if prev:
            if not now:
                self.addAtTail(val)
                return
            prev.next = Node(val, now)
        

    def deleteAtIndex(self, index: int) -> None:
        prev, now = None, self.head
        for _ in range(index):
            prev = now
            now = now.next if now and now.next else None
        if now:
            if not now.next:
                self.tail = prev
            if index == 0:
                self.head = now.next
            if prev:
                prev.next = now.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)