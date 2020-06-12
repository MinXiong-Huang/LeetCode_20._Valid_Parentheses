class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        data=[]

        for i in s:
            if i in '([{': #判斷正確順序
                data.append(i)
            else:
                if not data or dic[i] != data.pop():
                    return False
        return not data

#Example
s=Solution()
s.isValid("()[]{}")