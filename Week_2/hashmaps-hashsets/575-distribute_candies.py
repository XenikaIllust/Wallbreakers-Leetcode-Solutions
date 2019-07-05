"""
For this question, I formed a counter dict and then organized it. I extracted items from the dict with ascending
order until the amount of candies sister had was equal to the split value. I think the time complexity can
be further improved.
"""

from collections import Counter, OrderedDict

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        total = len(candies)
        split = total / 2
        types = set(candies)
        
        candies_types = Counter(candies)
        ordered_candies_types = OrderedDict(sorted(candies_types.items(), \
                                                        key=lambda item: item[1], reverse=False))
        
        sister = []
        while len(sister) != split:
            for (key, value) in ordered_candies_types.items():
                if len(sister) == split:
                    break
                if value > 0:
                    sister.append(key)
                    ordered_candies_types[key] -= 1
                
        return len(set(sister))
