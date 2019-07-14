"""
Generally a working solution but failing long test cases.
"""

from collections import defaultdict
from copy import copy

class Solution:
    def rob(self, nums: List[int]) -> int:
        def find_forbidden(nums, curr_ind, forbidden):         
            if curr_ind > 0 and curr_ind < len(nums) - 1:
                forbidden[curr_ind - 1] = True
                forbidden[curr_ind + 1] = True
            elif curr_ind == 0:
                forbidden[len(nums) - 1] = True
                forbidden[curr_ind + 1] = True
            elif curr_ind == len(nums) - 1:
                forbidden[curr_ind - 1] = True
                forbidden[0] = True
        
        def rec_rob(nums, curr_ind, mid, forbidden, total, max_total):
            find_forbidden(nums, curr_ind, forbidden)
            forbidden[curr_ind] = True
            total[0] += nums[curr_ind]
            print(nums[curr_ind], total)
            
            if total[0] > max_total[0]:
                max_total[0] = total[0]
            
            for i in range(curr_ind + 1, len(nums)):
                if forbidden[i] == None:
                    rec_rob(nums, i, mid + 1, copy(forbidden), copy(total), max_total)
        
        mid = len(nums) // 2
        
        max_total = [0]
        for i in range(len(nums)):
            forbidden = defaultdict(lambda: None)
            total = [0]
            rec_rob(nums, i, mid, forbidden, total, max_total)
                
        return max_total[0]
