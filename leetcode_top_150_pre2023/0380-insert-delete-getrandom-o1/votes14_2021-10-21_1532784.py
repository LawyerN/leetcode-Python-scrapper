class RandomizedSet:

    def __init__(self):
        self.elems = []
        self.indexes = {}
        

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
		# New element will be at the end of list
        self.indexes[val] = len(self.elems)
        self.elems.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        val_index = self.indexes[val]
        last = self.elems[-1]
		
		# We\'re swapping the removed element with the last element in the list.
		# The last element will move to the position of the element removed.
        if val_index < len(self.elems)-1:  # Make sure we\'re not already last element
            self.elems[val_index] = last
            self.indexes[last] = val_index
		
		# Remove the last element. This is O(1).
        self.elems.pop()
		
		# The removed element no longer has an index in the list. Update dictionary.
        del self.indexes[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.elems)