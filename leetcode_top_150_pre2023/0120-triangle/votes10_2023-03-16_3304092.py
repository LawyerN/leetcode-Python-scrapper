class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        list1=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for i,v in enumerate(row):
                list1[i]= v + min(list1[i],list1[i+1])
        return list1[0]
    #please upvote me it would encourage me alot