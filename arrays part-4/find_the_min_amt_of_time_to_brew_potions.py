from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill) # no. of wizards
        m = len(mana) # no. of potions
        current_time = 0 # Time at which each wizard starts crafting a potion
        time_lapsed_latest_potion = [] # Array to keep times taken by each wizard to craft last potion

        # Fill up the array by the time each wizard takes in crafting 1st potion
        for wizard_skill in skill:
            current_time += wizard_skill * mana[0]
            time_lapsed_latest_potion.append(current_time)

        # Now, iterate through rest of the potion [1, . . , m-1]
        for j in range(1, m):
            current_potion = mana[j]
           
            # Take the time at which the last wizard completes crafting his potion
            next_potion_start_time = time_lapsed_latest_potion[-1]
            
            # Greedy, iterate till 1st wizard while try reducing this next potion start time
            for i in range(n - 2, -1, -1):
                # Take whichever is max, as the potion cannot be idle whereas the wizard could be idle
                next_potion_start_time = max(time_lapsed_latest_potion[i], next_potion_start_time - current_potion * skill[i])
            
            # Once the start time is calculated craft the next potion using it with the wizards
            for i in range(n):
                next_potion_start_time += skill[i] * current_potion
                time_lapsed_latest_potion[i] = next_potion_start_time
        
        # Time taken would be by the time last wizard completes crafting last potion
        return time_lapsed_latest_potion[-1]
        