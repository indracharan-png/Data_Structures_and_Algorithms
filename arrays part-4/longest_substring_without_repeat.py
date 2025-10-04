class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        seen = set()
        ans = 0

        # Keep considering the character at right pointer to increased the length of the string
        while(right < n):
            # If there are any duplicates of the character at right pointer 
            if s[right] in seen:
                # Reduce the size of the current string till there aren't any duplicates
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                # Consider the character at right pointer into yout string
                seen.add(s[right])
            
            # Update the length
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans


            
        