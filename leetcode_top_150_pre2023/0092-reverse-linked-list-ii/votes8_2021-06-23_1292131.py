# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # a standard template code to reverse a linkedlist
        def reverse(head):
            if head is None or head.next is None:
                return head
            rest = reverse(head.next)
            head.next.next = head
            head.next = None
            return rest
        
        nodeL, nodeM, nodeR = None, None, None
        
        # if both left and right points to the same element, then there is no point of reversing
        if left == right:
            return head
        
        # Split the list into left, middle, and right part, 
        # such that the middle part needs to be reversed.
        temp = ListNode()
        temp.next = head
        nodeL = temp
        
        i = 0
        while i < right:
            if i + 1 == left:
                nodeM = temp.next
                temp.next = None
                temp = nodeM
            elif i + 1 == right:
                nodeR = temp.next
                temp.next = None
                temp = nodeR
                break
            temp = temp.next
            i += 1
        
        nodeL = nodeL.next
        
        # reverse the middle part
        nodeM = reverse(nodeM)
        
        # if left part exists then add middle part to the end of left part
        if nodeL:
            temp = nodeL
            while temp.next:
                temp = temp.next
            temp.next = nodeM
        else:
            nodeL = nodeM
        
        # add right part to the end of middle part
        temp = nodeM
        while temp.next:
            temp = temp.next
        temp.next = nodeR
        
        return nodeL