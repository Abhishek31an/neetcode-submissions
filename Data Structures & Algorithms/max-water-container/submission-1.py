class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        temp=0
        maxm=0
        while i<j:
            h=min(height[i],height[j])
            temp=h*(j-i)
            if temp>maxm:
                maxm=temp
            if height[i]>height[j]:
                j-=1
            elif height[i]<height[j]:
                i+=1
            else:
                i+=1
        return maxm