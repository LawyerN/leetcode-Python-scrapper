from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Step 2: Calculate the in-degree of each node
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        
        # Step 3: Perform topological sort
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for cycle
        if len(result) < numCourses:
            return []
        
        return result