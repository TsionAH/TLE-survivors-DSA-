# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        def revers(lists,val=''):
            
            if lists is None:
                return val
            val += str(lists.val)
            return revers(lists.next,val)
        val1 = revers(l1, val='')[::-1]
        val2 = revers(l2, val='')[::-1]
        l3 = str(int(val1)+ int(val2))
        
        dummy = ListNode(0)
        curr = dummy
        for i in l3[::-1]:
            curr.next = ListNode(int(i))
            curr = curr.next
        head = dummy.next
        return head


        