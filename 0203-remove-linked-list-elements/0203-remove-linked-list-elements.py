# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        temp = ListNode(next=head)
        prev = temp
        curr = head

        while curr :
            nex = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = nex
        return temp.next
