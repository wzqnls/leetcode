"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

"""
解题思路：
先将字母与数字的对应关系存到字典中
然后遍历s 
由于此题计数采用26进1的方式进行计算
故每一位数最终解决都需要相应乘以26的幂次方
"""

import string


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = string.letters[26:]
        dict_letters = {}
        count = 0
        for k, v in enumerate(letters):
            dict_letters[v] = k + 1
        for k, v in enumerate(s[::-1]):
            count += dict_letters[v] * (26**k)
        return count