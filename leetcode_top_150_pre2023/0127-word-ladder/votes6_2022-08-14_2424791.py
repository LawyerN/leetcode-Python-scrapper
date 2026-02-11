class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # BFS brutal force
        wordDict = set(wordList)
        if endWord not in wordDict: return 0    # impossible to find route
        
        wlen = len(beginWord)
        
        # how many steps to each word
        steps = {beginWord: 1}
        
        q = deque([beginWord])
        
        while len(q) > 0:
            word = q.popleft()
            step = steps[word]
            
            # change every single charactor
            for i in range(wlen):
                c = word[i]
                
                # \'a\' ~ \'z\'
                for t in string.ascii_lowercase:
                    if c == t: continue     # the chractor is the same 
                    
                    new_word = word[:i] + t + word[i + 1:]
                    if new_word == endWord: return step + 1
                    if new_word not in wordDict: continue
                    
                    # remove it from dictionary, 
										# so we won\'t go through the same word twice
                    wordDict.remove(new_word)        
                    steps[new_word] = step + 1
                    q.append(new_word)
                    
        return 0