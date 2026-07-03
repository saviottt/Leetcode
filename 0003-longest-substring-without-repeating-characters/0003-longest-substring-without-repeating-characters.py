class Solution(object):
    def lengthOfLongestSubstring(self, s):
        tem=[]
        a=0
        for c in s:
            if c in tem:
                del tem[:tem.index(c) + 1]
            tem.append(c)
            if len(tem)>a:
                a=len(tem)
        return a