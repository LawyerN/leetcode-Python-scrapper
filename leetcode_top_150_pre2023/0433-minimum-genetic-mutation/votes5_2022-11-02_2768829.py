class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        ta=[start]
        vis=defaultdict(lambda:0)
        dc=defaultdict(lambda:0)
        for x in bank:
            dc[x]=1
        lev=0
        while(len(ta)>0):
            # print(ta)
            tt=[]
            for a in ta:
                if(a==end):
                    return lev
                for i in range(8):
                    for c in("ACGT"):
                        x=a[:i]+c+a[i+1:]
                        if(dc[x]==1 and vis[x]==0):
                            tt.append(x)
                            vis[x]=1
            ta=tt
            lev+=1
        return -1