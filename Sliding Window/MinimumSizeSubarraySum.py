# 209. Minimum Size Subarray Sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        if sum(nums) < target:
            return 0

        n = len(nums)
        i = 0
        curSum = 0
        ans = 100001
        for j in range(n):
            curSum += nums[j]
            while curSum >= target:
                ans = min(ans, j - i + 1)
                curSum -= nums[i]
                i += 1
                
        return ans