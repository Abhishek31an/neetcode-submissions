class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(index,path,sum):
            if sum==target:
                ans.append(path[:])
                return
            if index==len(candidates) or sum>target:
                return 
            
            sum+=candidates[index]
            path.append(candidates[index])
            backtrack(index,path,sum)
            if path:
                n=path[-1]
                path.pop()
                sum-=n
            backtrack(index+1,path,sum)
    
        backtrack(0,[],0)
        return ans