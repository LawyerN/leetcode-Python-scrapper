class MedianFinder(object):

    def __init__(self):
        self.first = [] #max heap, to get the largest item in the first half
        self.second = [] #min heap, to get the smallest item in the second half
        

    def addNum(self, num):
        heapq.heappush(self.first, -num)
        heapq.heappush(self.second, -(heapq.heappop(self.first)))
        if len(self.first) < len(self.second): #always keep the first half of list is bigger/equal to the second one
            heapq.heappush(self.first, -(heapq.heappop(self.second)))
        

    def findMedian(self):
        if len(self.first) > len(self.second):
            return -(self.first[0]) #already heapified
        else:
            return (float(-(self.first[0]))+float(self.second[0]))/2 #already heapified