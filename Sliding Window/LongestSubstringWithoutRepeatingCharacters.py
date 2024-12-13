# 3. Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        right = 0
        maxLen = 0
        charSet = set()
        while right < n:
            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1
                maxLen = max(maxLen, right - left)
            else:
                charSet.remove(s[left])
                left += 1

        return maxLen