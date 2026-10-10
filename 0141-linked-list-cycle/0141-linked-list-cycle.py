# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowprt = head
        fastprt = head
        while fastprt and fastprt.next:
            slowprt = slowprt.next
            fastprt = fastprt.next.next
            if slowprt == fastprt:
                return True
        return False
        