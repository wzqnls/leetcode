"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

"""
解题思路：
主要在于找到在python中，3的幂的最大值，然后求余
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 4052555153018976267 % n == 0 
