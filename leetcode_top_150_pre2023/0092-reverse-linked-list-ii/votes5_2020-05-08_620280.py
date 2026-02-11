class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        cur, prev = head, None
        for _ in range(m-1):
            prev = cur
            cur = cur.next
        tail, con = cur, prev
        for _ in range(n-m+1):
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head