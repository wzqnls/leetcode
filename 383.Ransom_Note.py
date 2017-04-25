"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""

"""
解题思路：
将字符串转化为列表，遍历ransomNote
若magazine中有，则移除该元素
否则 return False
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lst_ransomNote = list(ransomNote)
        lst_magazine = list(magazine)
        for i in lst_ransomNote:
            if i in lst_magazine:
                lst_magazine.remove(i)
            else:
                return False
        return True
