class Solution:
    def encode(self, strs: List[str]) -> str:
        st=""
        for i,v in enumerate(strs):
            st+=v
            st+="@.!"
        return st

    def decode(self, s: str) -> List[str]:
        i=0
        c=0
        temp=[]
        while i<len(s)-2:
            if s[i]=="@" and s[i+1]=="." and s[i+2]=="!":
                temp.append(s[c:i])
                i=i+3
                c=i
            else:
                i+=1
        return temp