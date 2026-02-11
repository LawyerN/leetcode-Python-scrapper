from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a set of words for faster lookup
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # Initialize queue with the beginWord and set of visited words
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            # Dequeue the word and its level
            word, level = queue.popleft()
            
            # Iterate over each character in the word
            for i in range(len(word)):
                # Iterate over all possible lowercase letters
                for c in \'abcdefghijklmnopqrstuvwxyz\':
                    # Skip if the character is the same as in the original word
                    if c == word[i]:
                        continue
                    
                    # Create the new word by replacing the character at index i
                    newWord = word[:i] + c + word[i+1:]
                    
                    # Check if the new word is in the wordSet and has not been visited before
                    if newWord in wordSet and newWord not in visited:
                        # Check if the new word is the endWord
                        if newWord == endWord:
                            return level + 1
                        
                        # Enqueue the new word and its level
                        queue.append((newWord, level + 1))
                        
                        # Add the new word to the set of visited words
                        visited.add(newWord)
        
        # No transformation sequence exists
        return 0