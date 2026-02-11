class MedianFinder:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lowerhalf = [] # store the small half, top is the largest in the small part
        self.upperhalf = [] # store the large half, top is the smallest in the large part

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # The case for the first element, just add to the minheap
        if len(self.lowerhalf) == 0:
            heapq.heappush(self.lowerhalf, -num)
            return
        
        # Now choose where to add the new element 
        # If it is less than or equal the top of min heap, it can be accomodated under it else go to max heap
        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num) # Go to the max Heap 
            #(-ve sign because to implement max heap using the default heapq in python, we need to negate the values)
        else:
            heapq.heappush(self.upperhalf, num) # Go to the min Heap
            
        # Adjusting the balance
        
        # If the lowerhalf heap has more elements
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, - heapq.heappop(self.lowerhalf))
        
        # If the upperhalf heap has more elements
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, - heapq.heappop(self.upperhalf))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # If both heaps have same number of elements return the avg
        # If not, then the root of the one with more elements, is the answer
        
        if len(self.lowerhalf) == len(self.upperhalf):
            return (- self.lowerhalf[0] + self.upperhalf[0] )/2.0 
            # - sign because lowerhalf has negative value
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -float(self.lowerhalf[0])
        else:
            return float(self.upperhalf[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()