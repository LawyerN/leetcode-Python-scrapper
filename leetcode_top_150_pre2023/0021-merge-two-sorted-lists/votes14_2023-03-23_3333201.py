class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out=dummy=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                out.next=list1
                list1=list1.next
            else:
                out.next=list2
                list2=list2.next
            out=out.next
        if list1:
            out.next=list1
            list1=list1.next
        if list2:
            out.next=list2
            list2=list2.next
        return dummy.next