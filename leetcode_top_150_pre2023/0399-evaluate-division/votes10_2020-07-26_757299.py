class UnionFind:
    def __init__(self):
        self.content = dict()
        
    
    def find(self, x):
        origin = self.content[x]
        if origin[0] != x:
            node = self.find(origin[0])
            self.content[x] = (node[0], node[1] * origin[1])
        return self.content[x]
    
    def union(self, x, y, value):
        if x not in self.content:
            self.content[x] = (x, 1)
        if y not in self.content:
            self.content[y] = (y, 1)
        bb_x = self.find(x)
        bb_y = self.find(y)
        self.content[bb_x[0]] = (bb_y[0], bb_y[1] * value / bb_x[1])
    
    def div(self, x, y):
        if x not in self.content or y not in self.content:
            return -1
        
        bb_x = self.find(x)
        bb_y = self.find(y)
        
        if bb_x[0] != bb_y[0]:
            return -1
        return bb_x[1] / bb_y[1]
    
    def compact(self):
        for key in self.content:
            self.find(key)
            


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for eq, val in zip(equations, values):
            uf.union(eq[0], eq[1], val)
        
        uf.compact()
        
        return [uf.div(q[0], q[1]) for q in queries]