"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

"""
解题思路：
建立一个新的对应关系，增加小数字的一些组合

Note：只需要一个小数字在左边即可
    举例说明：
        9："IX"
        因为如果是8的话是三个小数字在右边 此时变为VIII
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        list_roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""
        
        for k, v in enumerate(list_num):
            while(num >= v):
                res += list_roman[k]
                num -= v
        return res
