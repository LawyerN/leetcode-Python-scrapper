class trie:
    def __init__(self):
        self.children=[None]*26
        self.isend=False
    def insert(self,word):
        for i in word:
            if self.children[ord(i)-ord(\'a\')]==None:
                self.children[ord(i)-ord(\'a\')]=trie()
            self=self.children[ord(i)-ord(\'a\')]
        self.isend=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def search(x,y,tre,s):
            if board[x][y]==\'#\':
                return 
            c=board[x][y]
            board[x][y]=\'#\'
            t=tre.children[ord(c)-ord(\'a\')]
            if t!=None:
                ss=s+c
                if t.isend:result.add(ss)
                if x>0:search(x-1,y,t,ss)
                if y>0:search(x,y-1,t,ss)
                if x<len(board)-1:search(x+1,y,t,ss)
                if y<len(board[0])-1:search(x,y+1,t,ss)
            board[x][y]=c
        
        m,n=len(board),len(board[0])
        if len(words)==0:
            return []
        t=trie()
        for w in words:
            t.insert(w)
        result=set()
        for i in range(m):
            for j in range(n):
                k=board[i][j]
                if t.children[ord(k)-ord(\'a\')]!=None:
                    search(i,j,t,"")
        
        return list(result)