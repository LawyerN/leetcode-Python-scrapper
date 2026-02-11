class UnionFind:
    def __init__(self, size: int) -> None:
        # Initially, all the elements will have themselves as the parent
        self.parent = [i for i in range(size)]
        # Which also means that their size will be 1
        self.size = [1 for _ in range(size)]

    def find(self, x: int) -> int:
        # If the parent of the x is not itself, recursively find the parent
        # And apply path compression by assigning the root as the parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        # Find the roots of x and y
        x_root = self.find(x)
        y_root = self.find(y)

        # If they both do not belong to the same set
        if x_root != y_root:
            # Check which one is smaller
            # Smaller one should have the bigger one as parent
            if self.size[x_root] < self.size[y_root]:
                # x now has y as parent and y\'s size has increased by the size of x
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]
            else:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialize UnionFind data structure for nums
        uf = UnionFind(len(nums))
        
        # Initialize a dictionary to store the indices of all integers
        index = dict()

        for i, num in enumerate(nums):
            # Ignore duplicates
            if num in index:
                continue

            index[num] = i

            # Perform union with num - 1 and num + 1, if seen
            if num - 1 in index:
                uf.union(i, index[num - 1])
            if num + 1 in index:
                uf.union(i, index[num + 1])

        # Find the largest set (include [0] in case the input has no elements)
        return max(uf.size + [0])