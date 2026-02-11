class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp=head
        dummy=pre=ListNode()
        while temp and temp.next:
            if temp.val==temp.next.val:
                while temp and temp.next and temp.val==temp.next.val:
                    temp=temp.next
                temp=temp.next
                pre.next=temp
            else:
                pre.next=temp
                pre=pre.next
                temp=temp.next
        return dummy.next