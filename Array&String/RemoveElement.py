class Solution(object):
    def removeElement(self, nums, val):
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        
        return index
