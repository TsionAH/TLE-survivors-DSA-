# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        1-2->3->4->5->
        |          |
        left       right 
        1->5->2->3->4->
             |     |         |
        left  right     
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # separet them 
        second = slow.next
        slow.next = None
        # reverse the half linked list
        prev = None
        curr = second
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # merge the reversed linked list prev is the head of the reversed 
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        # left = head
        # right = head
        # prev = head
        # while right.next:
        #     prev.next = right
        #     right = right.next
        # while left.next:
        #     curr = left.next
        #     left.next = right
        #     right.next = curr
        #     left = curr
        #     prev.next = None
        #     while right.next:
        #         prev.next = right
        #         right = right.next