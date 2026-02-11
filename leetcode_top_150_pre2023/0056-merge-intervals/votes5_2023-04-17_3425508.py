class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        list1=[intervals[0]]
        for i ,j in intervals[1:]:
            if list1[-1][1]>=i:
                list1[-1][1]=max(list1[-1][1],j)
            else:
                list1.append([i,j])
        return list1