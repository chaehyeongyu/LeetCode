class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        return x == rev
