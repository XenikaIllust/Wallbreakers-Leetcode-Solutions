"""
My solution uses a sliding window to find anagrams but it is unable to deal with an edge case where there are 
{"a": 20000, "b": 1} and p has {"a":10000}.
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = Counter(p)
        s_counts = Counter(s)
        
        print(len(p), len(s), p_counts, s_counts)
        
        return None
        
        start_indices = []
        
        # edge case where s and p are the same
        if len(p) == len(s) and len(p_counts) == len(s_counts):
            for key in p_counts.keys():
                if s_counts[key] != p_counts[key]:
                    return start_indices
                
            start_indices.append(0)
            return start_indices
        
        # sliding window
        for i in range(len(s) - len(p) + 1):
            substring_counts = Counter()
            invalid = False
            for j in range(i, i + len(p)):
                if p_counts[s[j]] > 0:
                    substring_counts.update({s[j]:1})
                else:
                    substring_counts = Counter()
                    break
            for key in substring_counts.keys():
                if p_counts[key] != substring_counts[key]:
                    invalid = True
                    break
            
            if invalid == False and len(substring_counts) > 0:
                start_indices.append(i)
            
        return start_indices
