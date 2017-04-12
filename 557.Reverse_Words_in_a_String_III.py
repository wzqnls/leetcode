"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Subscribe to see which companies asked this question.
"""

"""
解题思路：
将原字符串用空格进行切片存为列表
将列表中每个元素进行反转，然后合并即可
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s:str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split(' ')])
