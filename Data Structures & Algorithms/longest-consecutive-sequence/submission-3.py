class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxm=0
        count=1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                count+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                if count>maxm:
                    maxm=count
                count=1
        if count>maxm and len(nums)!=0:
            maxm=count
        return maxm