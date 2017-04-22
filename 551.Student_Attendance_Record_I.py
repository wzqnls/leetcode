"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:

	1.'A' : Absent.
	2.'L' : Late.
	3.'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
	Input: "PPALLP"
	Output: True
Example 2:
	Input: "PPALLL"
	Output: False
"""

"""
解题思路：
注意审题，超过一个A，两个连续的L 
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and 'LLL' not in s
