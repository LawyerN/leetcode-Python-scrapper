from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # Create a set of all valid genes in the bank for faster access
        bankSet = set(bank)
        
        # Define the possible mutations for each character
        options = [\'A\', \'C\', \'G\', \'T\']
        
        # Create a queue to store the genes to be checked
        queue = deque()
        queue.append(startGene)
        
        # Create a set to mark visited genes
        visited = set()
        visited.add(startGene)
        
        # Counter to keep track of the minimum mutations required to reach end gene
        count = 0
        
        # Perform BFS
        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j+1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            count += 1
        
        # If end gene not found
        return -1