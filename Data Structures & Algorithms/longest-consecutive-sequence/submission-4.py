class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        print(s)
        maxm=0
        for v in s:
            if v-1 not in s:
                count=1
                while v+count in s:
                    count+=1
                if count>maxm:
                    maxm=count
        return maxm