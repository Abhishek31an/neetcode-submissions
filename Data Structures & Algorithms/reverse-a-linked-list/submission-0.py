# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        new=ListNode(None)
        while curr!=None:
            curr2=ListNode(curr.val)
            curr=curr.next
            curr2.next=new.next
            new.next=curr2
        return new.next
        