import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        # An array to keep track of next appearing zeros in string
        next_zeros = [n] * n
        
        for i in range(n - 2, -1, -1):
            if s[i + 1] == '0':
                next_zeros[i] = i + 1
            else:
                next_zeros[i] = next_zeros[i + 1]
        
        output = 0

        for left in range(n):
            # Check if the starting position holding zero and update zero coutner
            if s[left] == '0': 
                zeros = 1
            else: 
                zeros = 0

            right = left
            while zeros * zeros <= n:
                next_zero_pos = next_zeros[right] if right < n else n # Set the next pointer to next closest zero position in string
                ones = next_zero_pos - left  - zeros # Find out no. of ones present in current partial string
                if ones >= zeros * zeros:
                    # Take the min. b/w best case scenario and no. of excess ones in current partial string scenario
                    output += min(
                        next_zero_pos - right, 
                        (ones - zeros**2) + 1
                        )
                right = next_zero_pos
                zeros += 1
        
        return output



        






        