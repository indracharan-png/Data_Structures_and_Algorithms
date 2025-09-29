class Solution:
    def subarrayXor(self, arr, k):
        size = len(arr)
        output = 0
        prefix_xor_map = {} # A dictionary to keep track of previously computed xor's
        curr_xor = 0
        
        for i in range(size):
            curr_xor ^= arr[i]
            
            # Add current substring if it's equal to target
            if curr_xor == k:
                output += 1
                
            # Compute the value required to arrive at target
            required_val = curr_xor ^ k
            # Look for the required value from previously visited prefix's xors
            output += prefix_xor_map.get(required_val, 0)
            # Record the occurence of running xor value in dictionary
            prefix_xor_map[curr_xor] = prefix_xor_map.get(curr_xor, 0) + 1
            
        
        return output
            