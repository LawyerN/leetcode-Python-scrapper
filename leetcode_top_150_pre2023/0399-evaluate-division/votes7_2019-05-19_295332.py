class Solution:
    def calcEquation(self, eq: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph  =collections.defaultdict(list)
        cache = dict()
        def build_graph(eq,vals):
            for i,edge in enumerate(eq):
                s,e = edge
                graph[s].append((e,values[i]))
                graph[e].append((s,1/values[i]))
        
        def query(s,e):
            q = collections.deque([(s,1.0)])
            visited = set()
            if s not in graph or e not in graph:
                cache[(s,e)] = -1
                cache[(e,s)] = -1
                return 
            while q:
                node,value = q.popleft()
                if node == e:
                    cache[(s,node)] = value
                    cache[(node,s)] = 1 / value
                    return 
                else:
                    for nb,prod in graph[node]:
                        if nb not in visited:
                            q.append((nb,value*prod))
                            visited.add(nb)
                            
            cache[(s,e)] = -1
            return                             
        res = []
        build_graph(eq,values)        
        for s,e in queries:
            if (s,e) not in cache:
                query(s,e)
            res.append(cache[(s,e)])
        return res