class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for let in t:
            if i==len(s):
                return True
            if s[i]==let:
                i+=1
        return i==len(s)
    #please upvote me it would encourage me alot