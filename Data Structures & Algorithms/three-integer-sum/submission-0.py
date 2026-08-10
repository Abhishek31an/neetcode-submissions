class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        ans=[]
        for i,v in enumerate(nums):
            map=set()
            target=0-nums[i]
            for j in range(i+1,len(nums)):
                diff=target-nums[j]
                if diff in map:
                    temp2=[nums[i],nums[j],diff]
                    if temp2 not in ans:
                        ans.append(temp2)
                map.add(nums[j])
        return ans
