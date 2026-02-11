class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = \'\'.join(c for c in s if c.isalnum()).lower()
        # Check if string is equal to its reverse
        return s == s[::-1]