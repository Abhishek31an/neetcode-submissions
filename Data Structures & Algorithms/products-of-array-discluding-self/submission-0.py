class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=0
        ans=1
        for i,v in enumerate(nums):
            if v==0:
                count+=1
            else:
                ans*=v
        temp=[0]*len(nums)
        if count>1:
            return [0]*len(nums)
        elif count==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    temp[i]=ans
                else:
                    temp[i]=0
            return temp
        else:
            for i in range(len(nums)):
                temp[i]=int(ans/nums[i])
            return temp