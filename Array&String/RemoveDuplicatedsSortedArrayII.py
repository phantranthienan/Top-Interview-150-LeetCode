# 80. Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if j == 1 or nums[j] != nums[i - 1]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1
