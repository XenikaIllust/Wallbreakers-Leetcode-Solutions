'''
For this solution, I recognized that using Counter would reduce a lot of code that needed
to be written. As long as there are more than 1 jewels in the counter for any jewel type,
then it can be counted into the number of stones which are jewels.
'''

from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counts = Counter(J)
        
        jewel_in_stones_count = 0
        for l in S:
            if counts[l] > 0:
                jewel_in_stones_count += 1
                
        return jewel_in_stones_count
