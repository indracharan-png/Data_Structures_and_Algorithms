from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort the give array in-place
        nums.sort()
        size = len(nums)

        output = 0

        # Set the third side pointer to always the largest value in array
        for k in range(size - 1, 1, -1):
            # First side pointer
            i = 0
            # Second side pointer
            j = k - 1
            
            # Try different combinations of first and second side
            while(i < j):
                # Shrink the window on left end if identity does not satisfy 
                if nums[i] + nums[j] <= nums[k]:
                    i += 1
                else:
                    # Consider all the first side values on and in between the first and second side
                    output += j - i
                    j -= 1
            
        return output



        