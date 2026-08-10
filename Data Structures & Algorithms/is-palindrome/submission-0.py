class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for c in s:
            if c.isalnum():
                check += c.lower()
        return check == check[::-1]