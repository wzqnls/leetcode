"""
Given an integer, write a function to determine if it is a power of two.
"""

"""
解题思路：
我的方法就不放出来了，有点蠢
不过看到一个非常赞的解决办法，分享出来

https://discuss.leetcode.com/topic/27934/python-one-line-solution/3
以下内容摘于上面的地址

n & n - 1 removes the left most bit of n. If an integer is power of 2, there is a single bit in the binary representation of n.
e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0, also 16 != 0, based on these facts there is only one bit in b10000, so 16 is power of 2.

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)
