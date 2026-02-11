# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(length//k):
            curr = prev.next
            for j in range(k-1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
            prev = curr
        return dummy.next