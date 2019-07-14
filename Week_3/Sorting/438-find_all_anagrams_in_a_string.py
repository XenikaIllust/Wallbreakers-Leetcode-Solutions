"""
Sorting solution, but still cannot solve edge case.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = list(p)
        p.sort()
        
        start_indices = []
        
        i = len(p) - 1
        while i < len(s):
            subs = []
            
            for j in range(i - (len(p) - 1), i + 1):
                subs.append(s[j])
                
            subs.sort()
            
            if subs == p:
                start_indices.append(i - (len(p) - 1))
            
            i += 1
            
        return start_indices
