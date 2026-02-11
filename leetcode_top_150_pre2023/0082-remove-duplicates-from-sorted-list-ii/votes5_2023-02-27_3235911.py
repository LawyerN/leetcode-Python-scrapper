class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        d={}
        temp=head
        while temp!=None:
            if temp.val in d:
                d[temp.val]+=1
            else:
                d[temp.val]=1
            temp=temp.next
        temp=head
        L=ListNode()
        temp2=L
        while temp!=None:
            if temp.next==None and d[temp.val]>1:
                temp2.next=None
            if d[temp.val]>1:
                temp=temp.next
            else:
                temp2.next=temp
                temp2=temp2.next
                temp=temp.next
        return L.next