from collections import deque
def hashword(word):
    h=0
    c=1
    for i in word:
        h+=c*(ord(i)-97)
        c=c*26
    return h
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d={}
        for i in range(len(wordList)):
            d[hashword(wordList[i])]=0
        h=hashword(beginWord)
        q=deque()
        q.append(h)
        f=hashword(endWord)
        q=deque()
        q.append([h,1])
        if h in d:
            d[h]=1
        while q:
            x=q.popleft()
            h=x[0]
            ans=x[1]
            if h==f:
                return ans
            c=1
            for i in range(10):
                for j in range(26):
                    y=h-(((h%(c*26))//c)*c)+(c*j)
                    if y in d:
                        if d[y]==0:
                            d[y]=1
                            q.append([y,ans+1])
                c=c*26
        return 0