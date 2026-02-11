class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = defaultdict(dict)
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        
        # Helper function to perform DFS and find the path value
        def dfs(start, end, visited):
            # If we have already visited this node or it doesn\'t exist in the graph, return -1.0
            if start in visited or start not in graph:
                return -1.0
            # If we have reached the end node, return the path value
            if start == end:
                return 1.0
            # Mark the current node as visited
            visited.add(start)
            # Traverse the neighbors and find the path value recursively
            for neighbor, value in graph[start].items():
                path_value = dfs(neighbor, end, visited)
                # If we have found a valid path, return the product of the current value and path value
                if path_value != -1.0:
                    return value * path_value
            # If we haven\'t found a valid path, return -1.0
            return -1.0
        
        # Calculate the answer for each query
        result = []
        for query in queries:
            start, end = query
            # Perform DFS to find the path value
            result.append(dfs(start, end, set()))
        
        return result