m = len(nums1)
        n = len(nums2)
		# i.e. competition producing smallest sum
        comp = []
        result = []
        
        def addToComp(i,j):
            if i < m and j < n:
                heapq.heappush(comp, (nums1[i] + nums2[j], i, j))
        
        for i in range(m):
            heapq.heappush(comp, (nums1[i] + nums2[0], i, 0))
            
        while len(result) < k and comp:
            _, i, j = heapq.heappop(comp)
            result.append([nums1[i], nums2[j]])
            addToComp(i, j+1)
        return result