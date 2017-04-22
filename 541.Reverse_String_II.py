"""
Given a string and an integer k, 
you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Example:
	Input: s = "abcdefg", k = 2
	Output: "bacdfeg"

Restrictions:
	The string consists of lower English letters only.
	Length of the given string and k will in the range [1, 10000]
"""

"""
解题思路：
先将列表按2k长度进行分割，并存入新的列表
遍历新列表，针对两种情况进行处理
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        lst = [s[i: i + 2*k] for i in range(0, len(s), 2*k)]
        for i in lst:
            length = len(i)
            if length <= k:
                res += i[::-1]
            else:
                temp = i[:k][::-1] + i[k:]
                res += temp
        return res
