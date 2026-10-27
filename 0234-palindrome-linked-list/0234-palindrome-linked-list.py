# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        prev = None
        left = head
        right = head
        while right and right.next:
            right = right.next.next
            left = left.next
        if right:
            left = left.next
        curr = left
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        right = head
        while prev and right:
            if right.val != prev.val:
                return False
            right = right.next
            prev = prev.next
        return True