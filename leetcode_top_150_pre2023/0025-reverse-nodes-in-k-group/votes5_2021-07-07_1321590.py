class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        def reverse(head, m, n):
 
            prev = None
            curr = head
            i = 1
            while curr is not None and i < m:
                prev = curr
                curr = curr.next
                i = i + 1

            start = curr
            end = None
            while curr is not None and i <= n:
                next = curr.next
                curr.next = end
                end = curr
                curr = next
                i = i + 1

            start.next = curr
            if prev is None:
                head = end
            else:
                prev.next = end

            return head
        n=0
        cur = head
        while cur:
            cur=cur.next
            n+=1
        for i in range(1,n+1,k): 
            if i+k-1<=n:
                head = reverse(head, i, i+k-1)
        return head