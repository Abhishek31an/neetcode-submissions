class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i,v in enumerate(strs):
            key=tuple(sorted(v))
            if key in ans:
                ans[key].append(v)
            else:
                ans[key]=[v]
        return list(ans.values())