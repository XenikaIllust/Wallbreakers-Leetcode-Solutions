"""
For this question, I used a result counter to keep track of counts. If any count > 1
(repeat), break loop and return false. Else return true.
"""

from collections import Counter

class Solution:
    def isHappy(self, n: int) -> bool:
        result_counter = Counter()
        
        prev_res = n
        
        while prev_res != 1:
            result_counter.update({prev_res: 1})
            res = 0
            for i in str(prev_res):
                res += int(i) ** 2
                
            if result_counter[res] > 1:
                return False
            
            prev_res = res
            
        return True
