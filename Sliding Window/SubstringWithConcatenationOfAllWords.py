# 30. Substring with Concatenation of All Words

from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount
        sLen = len(s)
        result = []
        
        wordDict = Counter(words)
        
        for i in range(0, sLen - totalLen + 1):
            curDict = defaultdict(int)
            for j in range(i, i + totalLen, wordLen):
                curWord = s[j:j + wordLen]
                if curWord not in wordDict:
                    break

                curDict[curWord] += 1
                if curDict[curWord] > wordDict[curWord]:
                    break

                if j + wordLen == i + totalLen:
                    result.append(i)
        
        return result