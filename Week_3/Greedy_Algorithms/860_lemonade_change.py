"""
The list cannot be sorted because the solution is False as long as I cannot give change back to the customer at 
any point. To make this fast, I wanted to use a Counter to keep track of counts of dollar types. I iterate over a priority list and gather up a sum using a greedy method.
"""

from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:       
        price = 5
        priority = [20,10,5]
        
        wallet = Counter()
        for bill in bills:
            wallet.update({bill: 1})
            
            change = bill - price
            sum = 0
        
            if change > 0:
                for p in priority:
                    while change - sum >= p and wallet[p] > 0:
                        sum += p
                        wallet.update({p: -1})
                if sum != change:
                    return False
        
        return True
