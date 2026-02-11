class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tmp = [0] * (len(citations) + 1)
		
        for i in range(len(citations)):
            if citations[i] > len(citations):
                tmp[len(citations)] += 1
            else:
                tmp[citations[i]] += 1

        sum_ = 0
        for i in range(len(tmp) - 1, -1, -1):
            sum_ += tmp[i]
            if sum_ >= i:
                return i