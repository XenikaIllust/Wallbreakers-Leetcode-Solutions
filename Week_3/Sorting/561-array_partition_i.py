"""
Solution implemented using sorting
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        total = 0
        for i in range(0, len(nums)-1, 2):
            total += min(nums[i], nums[i+1])
            
        return total
