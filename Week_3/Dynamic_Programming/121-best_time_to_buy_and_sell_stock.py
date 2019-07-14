"""
I used a counter that gradually shrinks when elements are removed from it. I can immediately retrieve the highest value in the
remaining list because the counter is sorted in reverse order. The highest selling stock price obtained from the counter guarantees
that the profit is maximized for every stock price that is bought. 
"""

from collections import Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_rev = prices.copy()
        prices_rev.sort(reverse=True)
        price_counter = Counter(prices_rev)
        
        print(price_counter)
        
        max_profit = 0
        for price in prices:
            if price_counter[price] == 1:
                del price_counter[price]
            else:
                price_counter.update({price: -1})
                
            try:
                profit = list(price_counter.keys())[0] - price
                
                if profit > max_profit:
                    max_profit = profit
            except:
                continue
                
        return max_profit
