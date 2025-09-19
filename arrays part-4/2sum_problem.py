from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        # Map all the elements to their respective indices
        index_map = {}
        for i in range(size):
            index_map[nums[i]] = i
        
        # Iterate over the array
        for i in range(size):
            initial_val = nums[i]
            # Substracting the current element value from target gives the deficit value that is required
            deficit_val = target - initial_val
            # See if that deficit value exists in the dictionary and make sure deficit and initial are not at same position
            if deficit_val in index_map and index_map[deficit_val] != i:
                return [i, index_map[deficit_val]]
        
        return []