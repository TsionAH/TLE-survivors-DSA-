# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        curr = dummy
        count = 0
        while curr:
            
           
            curr = curr.next
            count += 1
        newcurr = dummy
        index  =0
        while newcurr.next:
            if index == count - n -1:
                newcurr.next = newcurr.next.next
                return dummy.next
            else:
                newcurr = newcurr.next
                index += 1
        return dummy.next
		
