class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0]))
        count = 1
        prev_end = points[0][1]
        
        for x,y in points[1:]:
            if x<=prev_end:
                prev_end = min(y, prev_end)
                continue
                
            prev_end = y
            count+=1
        return count