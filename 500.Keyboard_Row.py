"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


Example 1:
	Input: ["Hello", "Alaska", "Dad", "Peace"]
	Output: ["Alaska", "Dad"]

Note:
	1.You may use one character in the keyboard more than once.
	2.You may assume the input string will only contain letters of alphabet.
"""

"""
解题思路：
将字母表分别存到三个集合中
遍历输入列表，并将每个元素进行字符转小写和去重操作
通过两个集合的并集计算进行判断
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        first_line = set("qwertyuiop")
        second_line = set("asdfghjkl")
        third_line = set("zxcvbnm")
        
        for every_word in words:
            deal_word = set(every_word.lower())
            
            if deal_word | first_line == first_line:
                result.append(every_word)
            elif deal_word | second_line == second_line:
                result.append(every_word)
            elif deal_word | third_line == third_line:
                result.append(every_word)
        return result
