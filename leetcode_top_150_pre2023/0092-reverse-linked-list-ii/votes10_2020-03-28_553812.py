# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n:
            # Quick response for empty reverse interval
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        cur, prev = head, dummy_head
        cur_idx = 1
        
        # left sentry is the the m-th node
        # right sentry is the the n-th node
        left_sentry, right_sentry = None, None
        
        # left junction is the (m-1)-th node
        # right junction is the (n+1)-th node
        left_junction, right_junction = None, None
        
        rev = False
        
        while cur:
            
            if rev:
                # now we are in reverse interval
                
                # Backup original next node
                ori_next = cur.next
                
                # Let current node point to previous node
                cur.next = prev
                
                # Update previous node
                # Update current point to original next node
                prev = cur
                cur = ori_next
                
                # Handle for right junction node
                if cur_idx == n:
                    right_sentry = prev
                    right_junction = cur

                    # Construct new linkage based on left junction and right junction
                    left_junction.next = right_sentry
                    left_sentry.next = right_junction

                    # turn off reverse flag
                    rev = False              
                
                
            else:
                # now we are in normal interval
                
                # Handle for left junction node
                if cur_idx == m:
                
                    left_sentry = cur
                    left_junction = prev
                    
                    # turn on reverse flag
                    rev = True


                # Update previous node
                # Update current point to original next node
                prev = cur
                cur = cur.next
            
            
  
            # update visiting index
            cur_idx +=1
            
        return dummy_head.next