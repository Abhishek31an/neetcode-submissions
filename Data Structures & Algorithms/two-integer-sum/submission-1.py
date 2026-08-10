class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            new=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==new:
                    return [i,j]
                    break
        