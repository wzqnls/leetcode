"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
    1.The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    2.You could assume no leading zero bit in the integer’s binary representation.

    Example 1:    
        Input: 5
        Output: 2
        Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
        
    Example 2:
        Input: 1
        Output: 0
        Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

"""
解题思路：
利用num与位数相同的二进制数进行异或运算
eg：
    1010
    1111
--> 0101
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_str = bin(num)
        deal_len_str = len(bin) - 2
        mid = '0b' + '1' * deal_len_str
        return int(mid, 2) ^ num
