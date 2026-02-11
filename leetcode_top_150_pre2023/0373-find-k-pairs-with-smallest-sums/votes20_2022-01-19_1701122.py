class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        heapq.heapify(hq)
        
        # add all the pairs that we can form with
        # all the (first k) items in nums1 with the first
        # item in nums2
        for i in range(min(len(nums1), k)):
            heapq.heappush(hq, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))

        # since the smallest pair will
        # be the first element from both nums1 and nums2. We\'ll
        # start with that and then subsequently, we\'ll pop it out
        # from the heap and also insert the pair of the current
        # element from nums1 with the next nums2 element
        out = []
        while k > 0 and hq:
            _, n1, n2, idx = heapq.heappop(hq)
            out.append((n1, n2))
            if idx + 1 < len(nums2):
                # the heap will ensure that the smallest element
                # based on the sum will remain on top and the
                # next iteration will give us the pair we require
                heapq.heappush(hq, (n1+nums2[idx+1], n1, nums2[idx+1], idx+1))
            k -= 1
                
        return out