class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        p1, p2 = None, head
        for _ in range(left - 1):
            p1, p2 = p2, p2.next
        
        p4, p5 = p2, p2.next
        for _ in range(right - left):
            p5.next, p4, p5 = p4, p5, p5.next

        p2.next = p5
        if p1:
            p1.next, p4 = p4, head
        
        return p4