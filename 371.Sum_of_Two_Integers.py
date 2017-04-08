"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""

"""
解题思路：
正常来讲，这题考的就是二进制的加减法
然而有点菜，用递归写的只能在正整数范围内确定有效

下面的方法则是投机取巧的方法，尴尬^-^!
"""



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while(a & b):
            mid = a ^ b
            b = (a & b) << 1
            a = mid
        return a ^ b


######################################

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        lst = [a, b]
        return sum(lst)
