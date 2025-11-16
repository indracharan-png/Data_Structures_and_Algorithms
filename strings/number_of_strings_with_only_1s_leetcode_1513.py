class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        left, right = 0, 0
        output = 0

        # Outer loop to determine the start of substrings with 1's
        while(left < n):
            # Do not worry about 0's as they should not be part of substring
            if s[left] == '0':
                left += 1
                continue
            # You encountered an 1, so intialize the right pointer for substring building
            right = left
            # Keep extensing the substring as long as ones appears consecutively
            while(right < n and s[right] == '1'):
                # Add up all possible substrings where 1 at right most end included
                output += (right - left + 1) % mod
                output % mod
                right += 1
            # Increment the left pointer to right's position
            left = right
        
        return output % mod

        





        