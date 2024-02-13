class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strip non-alphanumeric characters.
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        return s == s[::-1]


