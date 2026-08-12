# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        ans=[]
        i=1
        while q:
            temp=[]
            i=len(q)
            while q and i!=0:
                curr=q.popleft()
                if curr!=None:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                i-=1
            if temp:
                ans.append(temp)
        return ans
