"""
With a counter, I can check in O(1) time if any number's count is 0 (lost number) or 2 (duplicate number).
"""

from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        
        duplicate = -1
        lost = -1
        
        for i in range(1, len(nums)+1):
            if nums_count[i] == 0:
                lost = i
            if nums_count[i] == 2:
                duplicate = i
                
        return [duplicate, lost]
