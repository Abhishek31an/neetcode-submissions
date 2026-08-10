from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=Counter(nums)
        ans2=ans.most_common(k)
        temp=[]
        for i,v in ans2:
            temp.append(i)
        return temp