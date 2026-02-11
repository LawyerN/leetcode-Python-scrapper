class Solution:
    def kSmallestPairs(self, n1: List[int], n2: List[int], k: int) -> List[List[int]]:
        if not n1 or not n2: return []
        
        heap = []
        for i in range(len(n1)):                                  
            heapq.heappush(heap, (n1[i] + n2[0], i, 0))           #Step 1
            
        result = []
        while heap and k > 0:                                     
            _, i, j = heapq.heappop(heap)                         #Step 2
            result.append([n1[i],n2[j]])                          #Step 3
            
            if j+1 < len(n2):                                     #Step 4
                heapq.heappush(heap, (n1[i]+n2[j+1],i, j+1))      #Step 5
            k-=1
        return result