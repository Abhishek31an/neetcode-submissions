class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in range(len(s)):
            temp=ord(s[i])
            if (temp>=97 and temp<=122) or (temp>=48 and temp<=57):
                t+=s[i]
            elif temp>=65 and temp<=90:
                t+=chr(temp+32)
        if t==t[::-1]:
            return True
        else:
            return False