# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowptr = head
        fastptr = head

        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                break
        if fastptr is None or fastptr.next is None:
            return None
        slowptr = head
        while slowptr != fastptr:
            slowptr = slowptr.next
            fastptr = fastptr.next
            
        return slowptr
