from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=Counter(nums)
        print(ans)
        for k,v in ans.items():
            if v>1:
                return True
        return False