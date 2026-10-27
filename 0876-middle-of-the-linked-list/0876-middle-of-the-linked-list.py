# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        onCount = head
        curr = head
        count = 0
        while onCount:
            onCount = onCount.next
            count += 1
        midIndex = count//2
        count2 = 0
        
        while curr:
            if count2 == midIndex:
                return curr
            else:
                curr = curr.next
                count2 += 1
        return curr