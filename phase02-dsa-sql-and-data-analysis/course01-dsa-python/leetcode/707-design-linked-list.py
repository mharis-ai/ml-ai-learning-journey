class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr is not None:
            if index == count:
                return curr.val
            count += 1
            curr = curr.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        prev = None 
        count = 0
        while curr is not None:
            if index == count and prev is not None:
                prev.next = new_node
                new_node.next = curr
                return
            count += 1
            prev = curr
            curr = curr.next

        if index == count and prev is not None:
            prev.next = new_node
            return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return
        
        curr = self.head
        prev = None
        count = 0
        while curr is not None:
            if index == count and prev is not None:
                prev.next = curr.next
                return
            
            count += 1
            prev = curr
            curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)