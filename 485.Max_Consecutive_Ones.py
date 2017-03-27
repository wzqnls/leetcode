"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
	Input: [1,1,0,1,1,1]
	Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

"""
解题思路：
遍历整个列表，对每个值进行判断
若值为1，则对临时变量加一
若值为0，则将之前的临时变量存到结果列表中
遍历完最后一个元素，将count存到lst中保存
取lst的最大值即可
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        count = 0
        for i in nums:
            if i:
                count += 1 
            else:
                lst.append(count)
                count = 0
        lst.append(count)
        return max(lst)
