class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        vis=[[False for _ in range(c)] for _ in range(r)]
        sum=False
        def backtrack(i,j,k,path,sum):
            if k==len(word):
                return True
            if i<0 or j<0 or i>=r or j>=c or vis[i][j]:
                return False
            if board[i][j]!=word[k]:
                return False
            k+=1
            vis[i][j]=True
            path.append(board[i][j])
            sum= sum or backtrack(i,j+1,k,path,sum) or backtrack(i+1,j,k,path,sum) or backtrack(i,j-1,k,path,sum) or backtrack(i-1,j,k,path,sum)
            vis[i][j]=False
            if path:
                path.pop()
            return sum
        for i in range(r):
            for j in range(c):
                sum= sum or backtrack(i,j,0,[],sum)
        return sum