class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n
        
        max_points = 0
        for i in range(n):
            slopes = {}
            same = 1
            for j in range(i+1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    slope = float(\'inf\')
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
                else:
                    slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
            if not slopes:
                max_points = max(max_points, same)
            else:
                max_points = max(max_points, max(slopes.values())+same)
                
        return max_points