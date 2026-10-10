# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        count = 0
        prev = None
        curr = head
        while curr:
            curr = curr.next
            count += 1
        curr = head
        prev = None
        index = count - n 
        count2 = 0
        if index < 0:
            return head.next if head else None
        while count2 < index and curr is not None:
            prev = curr
            curr = curr.next
            count2 += 1
        if curr is None:
            return head
        if prev is None:
            head = curr.next
        else:
            prev.next = curr.next
        return head