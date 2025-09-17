from typing import List, Optional


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        size = len(nums)
        return self.merge_sort(0, size - 1, nums)

    def merge_sort(self, left: int, right: int, nums: List[int]) -> int:
        # Base Case
        if left >= right:
            return 0

        # Compute the mid point
        mid = int((left + right) / 2)
        # A variable to keep track of reverse pairs in this current part of list
        output = 0

        # Recursive call on left portion of list 
        output += self.merge_sort(left, mid, nums)
        # Recursive call on right portion of list
        output += self.merge_sort(mid + 1, right, nums)

        # Now merge the current portion of the array
        output +=  self.merge(left, mid, right, nums)
        return output
    

    def merge(self, left: int, mid: int, right: int, nums: List[int]) -> int:

        # A variable to keep track of reverse pairs
        cnt = 0

        # An index to keep track of positions in list to allocate the elements
        list_idx = left
        
        # Left and right arrays and their respective indices to compare them
        left_arr, left_idx = nums[left: mid+1], 0
        right_arr, right_idx = nums[mid+1: right+1], 0

        left_size, right_size = len(left_arr), len(right_arr)

        # Count reverse pairs from the above both sorted left and right arrays
        j = 0
        for i in range(left_size):
            while j < right_size and left_arr[i] > 2 * right_arr[j]:
                j += 1
            cnt += j
            
        while left_idx < left_size and right_idx < right_size:
            # Left element is smaller than right element
            if left_arr[left_idx] <= right_arr[right_idx]:
                nums[list_idx] = left_arr[left_idx]
                left_idx += 1
            else:   
                # Right element is smaller than left element
                nums[list_idx] = right_arr[right_idx]
                right_idx += 1

            list_idx += 1
        
        # Add remaining part of the left array
        while left_idx < left_size:
            nums[list_idx] = left_arr[left_idx]
            left_idx += 1
            list_idx += 1
        
        # Add remaining part of the right array
        while right_idx < right_size:
            nums[list_idx] = right_arr[right_idx]
            right_idx += 1
            list_idx += 1
        
        return cnt








        

        