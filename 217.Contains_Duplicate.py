"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
	and it should return false if every element is distinct.
"""

"""
解题思路：
将列表进行去重，再判断两个列表的长度
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (len(nums) > len(set(nums))) if nums else False
