"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

"""
解题思路：
将原列表进行去重
遍历去重后的列表，并计算其元素在原列表中的次数
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_list = list(set(nums))
        buff = 0
        for i in unique_list:
            temp = nums.count(i)
            if temp > buff:
                buff = temp
                maj_num = i
        return maj_num
        
