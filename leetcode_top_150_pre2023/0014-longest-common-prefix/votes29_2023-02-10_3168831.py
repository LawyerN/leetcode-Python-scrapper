class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this will be an answer
        pref = \'\'        
        # find min and max words among strs
        minWord = min(strs)
        maxWord = max(strs)

        # for iteration
        i = 0
        N = min(len(minWord), len(maxWord))
        
        while i < N:
            # if chars are equal
            if minWord[i] == maxWord[i]:
                # add this char to the answer
                pref += minWord[i]
            else:
                # if not, break
                break
            i += 1

        return pref