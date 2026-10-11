# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        # itrate 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        # reverse the half of the linkded list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # check the palindrom

        left,right = head,prev
        while right :
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
