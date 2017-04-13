"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

"""
解题思路：
参照1.Two Sum 解法，基本没什么出入
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_buff = {}
        for i in range(len(numbers)):
            if numbers[i] not in dict_buff:
                dict_buff[target - numbers[i]] = i
            else:
                return [dict_buff[numbers[i]]+1, i+1]

