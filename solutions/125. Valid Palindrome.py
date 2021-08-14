class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s=s.lower()
        s1=s[::-1]
        if(s==s1):
            return True
        return False
