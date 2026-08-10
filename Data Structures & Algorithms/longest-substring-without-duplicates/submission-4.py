class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        i=0
        l=0
        count=0
        maxm=0
        temp=set()
        while i<len(s):
            if s[i] not in temp:
                temp.add(s[i])
                count+=1
            else:
                while s[i] in temp:
                    temp.remove(s[l])
                    l+=1
                    count-=1
                temp.add(s[i])
                count+=1
            if count>maxm:
                maxm=count
            i+=1
        return maxm