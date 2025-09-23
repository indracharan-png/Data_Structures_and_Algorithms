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
    
    def optimized_fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)

        output = []
        
        # Sort the given array
        nums.sort()

        for i in range(size - 3):
            # Handle duplicates for 1st number
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i + 1, size - 2):
                # Handle duplicates for 2nd number
                if j > i+1 and nums[j] == nums[j-1]: continue

                # Set the two pointers at either ends of the remaining portion of array 
                left = j + 1
                right = size - 1

                while(left < right):
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum > target: 
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1 
                        # Handle the duplicates for 3rd and 4th number
                        while(left < right and nums[right] == nums[right + 1]):
                            right -= 1
                        while(left < right and nums[left] == nums[left - 1]):
                            left += 1
        
        return output

                    

                    

            
        
        