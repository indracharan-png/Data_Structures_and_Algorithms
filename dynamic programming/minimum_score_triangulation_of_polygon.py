from typing import List

class Solution:
    def minScoreTriangulation_topdown(self, values: List[int]) -> int:
        size = len(values)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        return int(self.helper(0, size - 1, values, dp))
    
    def helper(self, start_idx, end_idx, values, dp) -> float:
        # Base case:
        if end_idx - start_idx <= 1:
            return 0
        # CHeck if the sub-problem has already been sovled
        if dp[start_idx][end_idx] != 0:
            return dp[start_idx][end_idx]
        # If not yet computed, go on with the algorithm
        min_score = float('inf')

        # Check every cut between start and end
        for k in range(start_idx + 1, end_idx):
            # Calculate the current cut cost
            curr_val = values[start_idx] * values[k] * values[end_idx]
            # Divide into two sub problems and call the methods
            min_score = min(min_score, self.helper(start_idx, k, values, dp) + curr_val + self.helper(k, end_idx, values, dp))
        
        dp[start_idx][end_idx] = min_score
        return min_score 
    
    def minScoreTriangulation_bottomup(self, values: List[int]) -> int: 
        n = len(values)
        dp = [[0]*n for _ in range(n)]

        # gap = j - i
        for gap in range(2, n):           # need at least a triangle (gap >= 2)
            for i in range(0, n - gap):
                j = i + gap
                best = float('inf')
                for k in range(i + 1, j): # split at k
                    cost = values[i] * values[k] * values[j]
                    best = min(best, dp[i][k] + cost + dp[k][j])
                dp[i][j] = int(best)

        return dp[0][n - 1]
                    

        
    




        