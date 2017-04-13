"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
	who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
			For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
	1.N is a positive integer and won't exceed 10,000.
	2.All the scores of athletes are guaranteed to be unique.
"""

"""
解题思路：
首先对原列表进行降序排序
然后定义一个根据排名对照的列表
将两个列表的值进行zip操作，转化为字典
在字典中根据nums中的键，将对应的值取出即可
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        reversed_nums = sorted(nums)[::-1]
        buff = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [stmZ
        dict_relation = dict(zip(reversed_nums, buff))
        return map(dict_relation.get, nums)
