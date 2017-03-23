"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
解题思路：
利用字典的键值对翻转
假定其中成员为x，则另一成员为target - x
遍历一次列表即可
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        deal_dict = {}
        for i in range(len(nums)):
            if nums[i] not in deal_dict:
                deal_dict[target - nums[i]] = i
            else:
                return [deal_dict[nums[i]], i]
