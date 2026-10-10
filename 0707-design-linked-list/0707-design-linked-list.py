class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp is not None and count < index:
            temp = temp.next
            count +=1
        if temp is None or index < 0:
            return -1
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        
        curr = self.head
        prev = None
        count = 0
        while curr is not None and count < index:
            prev = curr
            curr = curr.next
            count += 1
        if  index < 0 or count != index:
            return
        
        if prev is None:
            new_node.next = self.head
            self.head = new_node
        else:
            prev.next = new_node
            new_node.next = curr

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        prev = None
        count = 0
        while curr is not None and count < index:
            prev = curr
            curr = curr.next
            count += 1
        if curr is None or index < 0:
            return
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)