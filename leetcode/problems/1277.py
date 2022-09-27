class Solution:
    """
    Leetcode Problem #1277
    
    Topics: Dynamic Programming
    """
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = matrix[i][j]

        squareSubmatrices = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if dp[i][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                squareSubmatrices += dp[i][j]
        
        return squareSubmatrices 