# 169. Majority Element
class Solution(object):
    def majorityElement(self, nums):
        major_element = None
        count = 0
        for num in nums:
            if count == 0:
                major_element = num
                count = 1
            elif major_element == num:
                count += 1
            else:
                count -= 1
        return major_element