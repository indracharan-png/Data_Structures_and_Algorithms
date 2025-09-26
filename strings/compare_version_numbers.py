import math

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the string at each occurence of '.' in both strings
        version1_arr = version1.split('.')
        version2_arr = version2.split('.')

        # Check for length differnce 
        deficit_len = len(version1_arr) - len(version2_arr)

        # Fill in the deficit length if it exists
        if deficit_len < 0:
            version1_arr.extend(['0'] * (deficit_len * -1))
        elif deficit_len > 0:
            version2_arr.extend(['0'] * deficit_len)
        
        # Now the size is same for both arrays for strings
        size = len(version1_arr)

        # Iterate through (left to right) and cast each string element to int type and compare 
        for i in range(size):
            v1 = int(version1_arr[i])
            v2 = int(version2_arr[i])
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
        

            
        