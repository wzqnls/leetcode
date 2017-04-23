"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""

"""
解题思路：
首先创建一个字典，存储数字和字符的对应关系 
分别是：
    1 'A'
    2 'B'
    .
    .
    .
    26 'Z'
然后对n进行26进制的转换

Note：
    当余数正好为0时，这特么就尴尬了。所以求余先减一，计算完再加一，避免被余成0   
"""

import string

class Solution(object):
    
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = string.letters[26:]
        dict_letters = {}
        string_res = ''
        for k, v in enumerate(letters):
            dict_letters[k+1] = v
        
        while n > 0:
            n -= 1
            string_res = dict_letters[n%26 + 1] + string_res
            n /= 26
        return string_res
        
