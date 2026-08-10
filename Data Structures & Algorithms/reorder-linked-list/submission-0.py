class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s=head
        f=head
        while f.next!=None and f.next.next!=None:
            s=s.next
            f=f.next.next
        mid=s
        s=s.next
        mid.next=None
        
        curr=s
        new=ListNode(None)
        while curr!=None:
            curr2=ListNode(curr.val)
            curr=curr.next
            curr2.next=new.next
            new.next=curr2
        s=new.next
        c1=head
        c2=s
        new=ListNode(None)
        c3=new
        while c1!=None or c2!=None:
            c3.next=c1
            c1=c1.next
            c3=c3.next
            
            if c2!=None:
                c3.next=c2
                c2=c2.next
                c3=c3.next
        head= new.next