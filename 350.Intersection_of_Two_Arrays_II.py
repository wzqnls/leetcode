"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
	Each element in the result should appear as many times as it shows in both arrays.
	The result can be in any order.
"""

"""
解题思路：
遍历nums1，判断每个元素是否存在于nums2
若存在，则将元素添加到结果集中，并在nums2中移除该元素
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i in nums2:
               res.append(i)
               nums2.remove(i)
        return res
