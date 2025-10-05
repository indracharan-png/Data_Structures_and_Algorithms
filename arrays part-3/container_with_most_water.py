from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_vol = 0

        while left < right:
            curr_vol = 0
            # Go greedy, take out the shorter rod between both and keep the taller one
            if height[left] > height[right]:
                curr_vol = height[right] * (right - left)
                right -= 1
            else:
                curr_vol = height[left] * (right - left)
                left += 1
            
            max_vol = max(max_vol, curr_vol)
        
        return max_vol
            



        