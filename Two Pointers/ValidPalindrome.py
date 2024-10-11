# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        only_alnum = filter(lambda c: c.isalnum(), s).lower()
        return only_alnum == only_alnum[::-1]