from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxheap = []   # Store the lower half
        self.minheap = []   # Store the larger half
        

    def addNum(self, num: int) -> None:
        # maxheap length is either equal or 1 greater than minheap length
        # always store negative value for maxheap
        heappush(self.maxheap, -num)
        
        # Convert to positive when retrieving from maxheap
        maxHeapTop = -heappop(self.maxheap)
        
        heappush(self.minheap, maxHeapTop)
        
        # Balance two heap
        if len(self.minheap) > len(self.maxheap):
            minHeapTop = heappop(self.minheap)
            heappush(self.maxheap,-minHeapTop)  
        
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            return -self.maxheap[0]