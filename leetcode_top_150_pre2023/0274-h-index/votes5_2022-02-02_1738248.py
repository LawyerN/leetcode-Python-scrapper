# Counting sort. Why? Number value range correlates with index.
# Given n papers, max H index is n. Have an additional one bucket to store all 
# papers that have > n citations. To align array index number with citation value, add one 
# more bucket. So total n+2 bucket. Then loop from index n to 0, accumulate the citation value
# along the way. If citations[i] >= i, i is the resulting max H index. 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        arr = [0] * (n + 2)
        for i in range(n):
            if citations[i] > n:
                arr[n + 1] += 1
            else:
                arr[citations[i]] += 1
            
        accSum = arr[n + 1]
        # iterate in reversed order from the last second one
        for i in range(n, -1, -1):
            accSum += arr[i]
            if accSum >= i:
                return i
        return 0