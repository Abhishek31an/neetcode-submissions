# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!=None:
            count+=1
            curr=curr.next
        if (count-n)==0:
            return head.next
        curr=head
        while curr!=None and (count-n)!=1:
            curr=curr.next
            count-=1
        if curr!=None and curr.next!=None:
            curr.next=curr.next.next
        
        return head