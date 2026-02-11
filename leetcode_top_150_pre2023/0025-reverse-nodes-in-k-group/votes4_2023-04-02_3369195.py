# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def link(self,a,b):
        r=a
        while a.next:
            a=a.next
        a.next=b

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        nh=head
        if head == None:
            return None
        while h.next!=None:
            second=nh
            nh=h.next 
            h.next=nh.next
            nh.next=second            
        return nh
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads=[]
        count=0
        x=head
        while x:
            if count%k==0:
                heads.append(x)
            x=x.next
            count+=1
        last=None
        if count%k!=0:
            last=heads.pop()
        newheads=[]
        for i in heads:
            c=0
            t=i
            while c<k-1:
                i=i.next
                c+=1
            i.next=None
            newheads.append(t)
        reverse=[]
        for i in newheads:
            reverse.append(self.reverseList(i))
        print(reverse)
        self.link(reverse[-1],last)
        for i in range(len(reverse)-2,-1,-1):
            self.link(reverse[i],reverse[i+1])
        return reverse[0]