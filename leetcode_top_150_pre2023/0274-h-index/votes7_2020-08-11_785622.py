class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        
        res = 0
        citations.sort(reverse = True)
        
        if citations[-1] >= len(citations):
            return len(citations)
        
        for i in range(1, len(citations)+1):
            if i > citations[i-1]:
                res = i-1
                break
        return res