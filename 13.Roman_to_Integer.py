"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

"""
解题思路：
先上wiki上面看看罗马数字的计算方式
https://zh.wikipedia.org/wiki/罗马数字

将罗马数字对应的符号与数值存到字典中
遍历给定罗马字符串
判断相邻想个数值的大小，若左边大于等于右边，那数值相加
若左边小于右边，那相加数值后，对之前的数进行双倍减去

同时需要给定一个初始的阿拉伯数字，由于在遍历的过程中，第一位数只用于判断，没有计算
所以将字符串第一个数值定为初始值
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        integer = dict_nums[s[0]]
        
        for k, v in enumerate(s[:-1]):
            if dict_nums[v] >= dict_nums[s[k+1]]:
                integer += dict_nums[s[k+1]]
            else:
                integer = integer + dict_nums[s[k+1]] - 2 * dict_nums[s[k]]
        return integer
