# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
			# keep l1 always point to the smallest node
            if l1.val > l2.val:
                l1, l2 = l2, l1
			# so each step, connect the current smallest node to the already linked list
            l1.next = self.mergeTwoLists(l1.next, l2)
		# short-circuit evaluation, if l1 not None, return l1, else, return l2
        return l1 or l2