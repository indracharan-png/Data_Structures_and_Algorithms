from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        # Map all the elements to their respective indices
        index_map = {}
        for i in range(size):
            if nums[i] in index_map:
                index_map[nums[i]].append(i)
            else:
                index_map[nums[i]] = [i]
        
        # Iterate over the array
        for i in range(size):
            initial_val = nums[i]
            # Substract the current element value from target, which gives the deficit value 
            deficit_val = target - initial_val
            # See if that deficit value exists in the dictionary
            if deficit_val in index_map:
                # Check if the deficit value is same as initial num value
                if deficit_val == initial_val:
                    # Make sure there are multiple copies of these deficit/initial value 
                    if len(index_map[deficit_val]) > 1:
                        return [index_map[deficit_val].pop(), index_map[deficit_val].pop()]
                else:
                    return [i, index_map[deficit_val].pop()]
        
        return []


        