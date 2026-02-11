class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = curHead = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curHead.next = l1
                curHead = curHead.next
                l1 = l1.next
            else:
                curHead.next = l2
                curHead = curHead.next
                l2 = l2.next
                
        curHead.next = l1 or l2
        return dummyHead.next