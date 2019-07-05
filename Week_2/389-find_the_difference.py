"""
Using a counter is sufficient as I can identify the element in t_counts that does not have the same 
frequency as the same element in s_counts.
"""

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = Counter(s)
        t_counts = Counter(t)
        
        for key in t_counts.keys():
            if t_counts[key] != s_counts[key]:
                return key
