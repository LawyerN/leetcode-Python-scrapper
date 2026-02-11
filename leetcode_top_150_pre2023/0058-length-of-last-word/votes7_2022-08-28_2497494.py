class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split(" ")
        lst=[ i for i in s if i!=""]
        a=lst[-1]
        return len(a)