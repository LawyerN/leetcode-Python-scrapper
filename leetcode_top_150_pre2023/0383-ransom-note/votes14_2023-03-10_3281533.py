class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote)=Counter(magazine)
    #please upvote me it would encourage me alot