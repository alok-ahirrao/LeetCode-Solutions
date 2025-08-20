class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp=[[0]*c for _ in range(r)]

        count=0

        for j in range(c):
            if(matrix[0][j]==1):
                dp[0][j]=1
                count+=1
        
        for i in range(1, r):
            if(matrix[i][0]==1):
                dp[i][0]=1
                count+=1

        for i in range(1, r):
            for j in range(1, c):
                if(matrix[i][j]==0):
                    continue
                elif dp[i-1][j]==0 or dp[i-1][j-1]==0 or dp[i][j-1]==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                
                count+=dp[i][j]
        
        return count
