from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        # Store the generated answers
        output = []
        # A set to make sure unique elements are getting counted
        seen = set()

        # Mapping elements to their indices
        index_map = {}
        for i in range(size):
            index_map[nums[i]] = i

        # Iterate through every initial 3 numbers combination
        for i in range(size):
            a = nums[i]
            for j in range(i+1, size):
                b = nums[j]
                for k in range(j+1, size):
                    c = nums[k]
                    # Compute the deficit value
                    d = target - (a + b + c)
                    # Check for it using index mapping and make sure its not from 3 initial nummbers
                    if d in index_map and index_map[d] not in (i, j, k):
                        temp_list = [a, b, c, d]
                        # Sort the list as the duplicates are possible in the arry
                        sorted_temp_list = sorted(temp_list)
                        temp_tuple = tuple(sorted_temp_list)
                        # Make sure this sequence is unique
                        if temp_tuple not in seen:
                            output.append(temp_list)
                            seen.add(temp_tuple)
                    
        return output
        