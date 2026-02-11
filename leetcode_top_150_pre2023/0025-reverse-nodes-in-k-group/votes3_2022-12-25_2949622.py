# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        # find lenght of list by going through it
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        
        # reverse l//k times k elements
        curr,dummy = head,ListNode()
        tail = dummy

        for i in range(l//k): # for every group of size k
            prev = None

            # reverse it
            for x in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp


            tail.next = prev # append the group to the dummy
            # get the pointer to the end
            for x in range(k): tail = tail.next 

        # append the remaining list
        tail.next = curr
        return dummy.next