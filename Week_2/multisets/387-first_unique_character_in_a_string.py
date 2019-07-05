"""
By using a Counter, the implementation for this question can be done in just a few lines. The first unique
character is found by iterating through the counter and finding the first letter that has a count of 1. If 
it cannot be found, return -1.
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_counts = Counter(s)
        
        for i, l in enumerate(s):
            if s_counts[l] == 1:
                return i
            
        return -1
