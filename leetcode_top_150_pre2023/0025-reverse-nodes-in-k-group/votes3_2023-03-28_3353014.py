# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=b=ListNode()
        i=0
        z=None
        #Reverse the k nodes
        while head:
            i=i+1
            if i<=k:
                x=head.next
                head.next=z
                z=head
                head=x
            #Assign the reversed nodes to the new links
            if i==k:
                b.next=z
                #Take pointer until end of the reversed nodes
                while b and b.next:
                    b=b.next
                z=None
                i=0
        #And finally reverse the nodes and assign the nodes
        zz=None
        while z:
            #Reverse
            g=z.next
            z.next=zz
            zz=z
            z=g
        #Assign the final nodes which are length is the less than k
        b.next=zz
        #The total link connection is in a then return a.next
        return a.next