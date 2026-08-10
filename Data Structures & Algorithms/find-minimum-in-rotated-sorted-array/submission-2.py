class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while i<j:
            mid=i+(j-i)//2
            if i==mid or j==mid:
                return min(nums[i],nums[j],nums[mid])
            if nums[i]<=nums[mid]<=nums[j]:
                return nums[0]
            elif nums[i]<nums[mid]:
                i=mid
            elif nums[mid]<nums[j]:
                j=mid
            
