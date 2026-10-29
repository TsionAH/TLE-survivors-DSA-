# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        sum1 = ''
        sum2 = ''
        prev1 = None
        prev2 = None
        curr1 = l1
        curr2 = l2
        while curr1:
            temp1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp1
        while curr2:
            temp2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = temp2
        while prev1:
            sum1 += str(prev1.val)
            prev1 = prev1.next
        while prev2:
            sum2 += str(prev2.val)
            prev2 = prev2.next
        ans = int(sum1) + int(sum2)
        ans = str(ans)
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(ans)-1,-1,-1):
            curr.next = ListNode(int(ans[i]))
            curr = curr.next

        head = dummy.next
        return head

        

