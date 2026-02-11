class RandomizedSet:
    ## RC ##
    ## APPROACH : HASHMAP ##
    #   1. Insertion operation in list is O(1) but not deletion
    #   2. So we create one Hashmap with key,index and other list
    #   3. for deleting we go to hashmap, get index, go to that index in list, swap that element with last element.
    #   4. save the index to last element in hashmap and delete list last element

    def __init__(self):
        self.lists = []
        self.hmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if(val in self.hmap):
            return False
        self.hmap[val] = self.length
        self.length += 1
        self.lists.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.hmap):
            return False
        index = self.hmap[val]
        self.hmap[self.lists[-1]] = index
        self.lists[index], self.lists[-1] = self.lists[-1], self.lists[index]
        self.lists.pop()
        self.hmap.pop(val)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        ri = random.randint(0, self.length - 1)
        return self.lists[ri]