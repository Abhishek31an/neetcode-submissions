class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        if len(nums)==1:
            if nums[0]==target: return 0
            else: return -1
        while i<j:
            mid=i+(j-i)//2
            if i==mid or j==mid:
                if nums[i]==target: return i
                if nums[j]==target: return j
                else: return -1
            if nums[i]<nums[mid]:
                if target>=nums[i] and target<=nums[mid]:
                    j=mid
                else:
                    i=mid
            elif nums[mid]<nums[j]:
                if target>=nums[mid] and target<=nums[j]:
                    i=mid
                else:
                    j=mid