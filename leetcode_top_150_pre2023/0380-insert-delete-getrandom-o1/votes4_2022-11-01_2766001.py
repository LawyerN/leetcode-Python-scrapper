import random
from sortedcontainers import SortedList
class RandomizedSet:
    def __init__(self):
        self.arr=SortedList([])
        self.dc=defaultdict(lambda:0)
    def insert(self, val: int) -> bool:
        if(self.dc[val]==1):
            return False
        self.dc[val]=1
        self.arr.add(val)
        return True
    def remove(self, val: int) -> bool:
        if(self.dc[val]==0):
            return False
        self.dc[val]=0
        self.arr.discard(val)
        return True
    def getRandom(self) -> int:
        x=random.randint(0,len(self.arr)-1)
        return(self.arr[x])