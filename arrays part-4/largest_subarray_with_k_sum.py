class Solution:
    def longestSubarray(self, arr, k):  
       size = len(arr)
       
       # Keep track of prefix sum and it's index in the array
       prefix_sum_dict = {}
       curr_sum = 0 # A variable to keep track of ongoing sum
       
       output = 0
       
       for i in range(size):
           curr_sum += arr[i]
           
           if curr_sum == k:
               output = max(output, i + 1)
               
           
           deficit_val = curr_sum - k
           
           # Check if the deficit value has already seen
           if deficit_val in prefix_sum_dict:
               output = max(output, i -  prefix_sum_dict[deficit_val])
               
           # Add the earliest seen current sum value into the dict
           if curr_sum not in prefix_sum_dict:
               prefix_sum_dict[curr_sum] = i
               
           
           
       
       return output
               
              
            
          
           
       
       
    
