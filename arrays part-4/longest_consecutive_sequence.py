from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        output = 0

        # Set up a set data stucture from the list
        for num in nums_set:
            # Always start from the first number in consecutive numbers
            if num-1 not in nums_set:
                len = 1
                # Compute next sequence of consecutive numbers
                while num + len in nums_set:
                    len += 1
                output = max(output, len)
        
        return output


        