from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        map=defaultdict(str)
        map['(']=')'
        map['{']='}'
        map['[']=']'
        stack=[]
        i=0
        while i<len(s):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if stack and map[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    return False
            i+=1
        if len(stack)==0:
            return True
        else:
            return False