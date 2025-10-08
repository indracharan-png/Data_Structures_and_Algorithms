from collections import deque, defaultdict
import heapq
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        is_filled = set() # This keeps track of already filled lakes
        heap = [] # An hashmap (idx, rains[idx]) that sortsthe lakes depending on earliest rain days
        next_rains = defaultdict(deque)

        output = []

        for i, lake in enumerate(rains):
            if rains[i] > 0:
                next_rains[lake].append(i)

        for i in range(n):
            lake = rains[i]
            # See if there's a rain in first place
            if  lake != 0:
                # Check if that lake is already filled
                if lake in is_filled:
                    return []

                is_filled.add(lake) # Add the lake into filled lakes
                next_rains[lake].popleft() # And pop its occurence from the heap

                # See if there's gonna be future rains on this particular lake
                if next_rains[lake]:
                    heapq.heappush(heap, (next_rains[lake][0], current_lake)) # Add it to heap by prioritizing its index
                output.append(-1) # Append the current lake output with -1
            else: 
                # If its a dry day, check if there's any lakes in heap
                if heap:
                    # Consider drying out the lake that will have earliest rain 
                    _, to_be_dried_lake = heapq.heappop(heap)
                    # Remove it from filled, as it is now dried
                    is_filled.remove(to_be_dried_lake)
                    # Append the dried lake to output array
                    output.append(to_be_dried_lake)
                else:
                    # If its a dry day and there are no lakes that needs drying, append the default value '1'
                    output.append(1)
        
        return output

                

                
                
                

    


                

        