"""
Having a counter and sorting it in reverse order makes the question really convenient and has less lines of code.
After that, its simply just about iterating through the sorted list and appending a new string according to
frequency.
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_counts = Counter(s)
        
        s_counts = sorted(s_counts.items(), key=lambda item: item[1], reverse=True)
        
        new_s = ""
        
        for word_cp in s_counts:
            for i in range(word_cp[1]):
                new_s += word_cp[0]
                
        return new_s
