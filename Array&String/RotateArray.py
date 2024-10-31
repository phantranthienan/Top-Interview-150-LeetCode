# 189. Rotate Array

class Solution(object):
    def rotate(self, nums, k):
        ans = []
        k = k % len(nums)
        ans = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = ans[i]

    def rotate2(self, nums, k):
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]