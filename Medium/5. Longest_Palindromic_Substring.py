class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            substr=s[i]
            for j in range(i+1,len(s)):
                substr+=s[j]
                if substr==substr[::-1]:
                     if len(substr)>len(res):
                          res=substr
        if len(res)==0:
             return s[0]
        if len(s)==2 and s[0]!=s[1]:
            return s[0]
        else:
             return res