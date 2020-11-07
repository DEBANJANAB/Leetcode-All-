# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=ListNode
        temp.next=head
        slow=temp
        fast=temp
        for i in range(1,n+2):
            fast=fast.next
        while fast is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return temp.next
