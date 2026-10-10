# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        middle = count // 2 
        curr = head
        count = 0
        if middle < 0:
            return head
        while count < middle and curr:
            curr = curr.next
            count += 1
        head = curr
        return head

        