"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

	12 + 92 = 82
	82 + 22 = 68
	62 + 82 = 100
	12 + 02 + 02 = 1
"""

"""
解题思路：
定义一个函数计算数值元素的平方和
定义一个列表用于存储平方和的结果集
在while中，若结果为1，返回True
若结果已存在于res中，说明已产生死循环，返回False
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def caculate(n):
            lst = [int(i) for i in str(n)]
            return sum(i**2 for i in lst)
    
        res = list()
        while True:
            buff = caculate(n)
            if buff == 1:
                return True
            if buff in res:
                return False
            res.append(buff)
            n = buff
