"""
Write a function that takes a string as input and returns the string reversed.

Example:
	Given s = "hello", return "olleh".

Subscribe to see which companies asked this question.
"""

"""
解题思路：
解法很多，切片比较方便
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
