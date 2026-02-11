def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q=[(beginWord,1)]
        for word,d in q:
            if word==endWord:
                return d
            for i in range(len(word)):
                for char in \'abcdefghijklmnopqrstuvwxyz\':
                    tmp=word[:i]+char+word[i+1:]
                    if tmp in wordList:
                        q.append([tmp,d+1])
                        wordList.remove(tmp)
        return 0