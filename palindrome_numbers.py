class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        rev=0
        original=x
        while x>0:
            last_digit=x%10
            rev=rev*10+last_digit
            x//=10
        if rev == original:
            return True
        else:
            return False