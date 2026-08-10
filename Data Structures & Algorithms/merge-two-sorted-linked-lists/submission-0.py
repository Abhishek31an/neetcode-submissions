# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1==None and list2==None:
            return None
        c1=list1
        c2=list2
        new=ListNode(None)
        c3=new
        while c1!=None and c2!=None:
            if c1.val<=c2.val:
                c3.next=c1
                c1=c1.next
                c3=c3.next
            elif c1.val>c2.val:
                c3.next=c2
                c2=c2.next
                c3=c3.next
        if c1==None and c2!=None:
            c3.next=c2
        elif c2==None and c1!=None:
            c3.next=c1
        return new.next
