class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtracking(curr: List[int],i:int):
            s=sum(curr)
            if s==target:
                res.append(curr)
            elif s<target:
                for j in range(i,len(can)):
                    backtracking(curr+[can[j]],j)
        backtracking([],0)
        return res