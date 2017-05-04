"""
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
	Input: "aba", "cdc"
Output: 3

Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
			because "aba" is a subsequence of "aba", 
			but not a subsequence of any other strings in the group of two strings. 

Note:
Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.
"""

"""
解题思路：
求两个字符串的最大非公共子序列的长度
两个字符串一样，则return -1
不一样的话，就返回长度更长的那个字符串长度
ps：这题感觉没有什么意义
"""

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
