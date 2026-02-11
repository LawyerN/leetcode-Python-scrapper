class Solution(object):
    def deleteDuplicates(self, head):
        if head is not None:
            if head.next is not None:
                if head.val == head.next.val:
                    headTemp = self.deleteDuplicates(head.next)
                    if headTemp is not None:
                        if head.val == headTemp.val:
                            if headTemp is not None:
                                return headTemp.next
                            return None
                    return headTemp
                else:
                    head.next = self.deleteDuplicates(head.next)
        return head