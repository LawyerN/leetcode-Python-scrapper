class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i starts at beginning of s and j starts at the end         
        i, j = 0, len(s) - 1
        # While i is still before j        
        while i < j:
            # If i is not an alpha-numeric character then advance i            
            if not s[i].isalnum():
                i += 1
            # If j is not an alpha-numeric character then advance i
            elif not s[j].isalnum():
                j -= 1
            # Both i and j are alpha-numeric characters at this point so if they do not match return the fact that input was non-palendromic
            elif s[i].lower() != s[j].lower():
                return False
            # Otherwise characters matched and we should look at the next pair of characters
            else:
                i, j = i + 1, j - 1
        # The entire stirng was verified and we return the fact that the input string was palendromic         
        return True