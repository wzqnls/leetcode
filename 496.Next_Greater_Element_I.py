"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, output -1 for this number.

Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]

Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]

Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""

"""
题目翻译：
给定两个数组nums1和nums2,nums1是nums2的子集
查找所有nums1中元素在nums2中临近的比这个值大的元素

这个值就是nums1中的x在nums2中的位置靠右第一个比x大的元素
如果找不到的话，就输出-1

下面两个例子的解释描述了具体过程，可重点参考
"""

"""
解题思路：
遍历nums1数组，查找每个元素在nums2中的位置
从元素在nums2中的位置往后开始遍历，寻找比此元素大的值

notes：考虑到边界条件，从x在nums2中的当前位置开始遍历，防止数组越界
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in findNums:
            index = nums.index(i)
            for j in nums[index:]:
                if j > i:
                    result.append(j)
                    break
            else:
                result.append(-1)
        return result
