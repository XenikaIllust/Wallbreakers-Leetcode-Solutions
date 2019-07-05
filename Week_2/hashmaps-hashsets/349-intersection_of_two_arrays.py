"""
Two counters is the ultimate solution. As long as one set is checked against another, 
and the key is not 0 (exists), then it is in the other set. 
"""

from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_counts = Counter(nums1)
        n2_counts = Counter(nums2)
        
        intersections = set()
        for key in n1_counts:
            if n2_counts[key] != 0:
                intersections.add(key)
        
        return list(intersections)
