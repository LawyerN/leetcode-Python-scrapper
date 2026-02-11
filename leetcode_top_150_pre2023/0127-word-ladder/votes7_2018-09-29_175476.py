class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([(beginWord, 1)])

        if endWord not in wordSet:
            return 0
        
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while q:
            current_word, current_length = q.popleft()
            for i in range(len(current_word)):
                for ch in \'abcdefghijklmnopqrstuvwxyz\':
                    new_word = current_word[:i] + ch + current_word[i+1:]
                    if new_word == endWord:
                        return current_length + 1
                    
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        q.append((new_word, current_length + 1))
        
        return 0