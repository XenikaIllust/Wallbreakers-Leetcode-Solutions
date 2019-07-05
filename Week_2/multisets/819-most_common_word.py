"""
I created a Counter with banned items. Adding new elements to the main Counter requires that it doesn't exist
in the banned Counter (ie count == 0). Using a counter for words and then sorting them according to reverse
order is powerful, because after sorting I can return the top item (the item with highest frequency).
"""

import re
from collections import Counter, OrderedDict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-zA-z]+", paragraph)
        
        banned = Counter(banned)
        words_count = Counter()
        
        for word in words:
            word = word.lower()
            if banned[word] != 0:
                continue
            else:
                words_count.update({word: 1}) 
                
        words_count = sorted(words_count.items(), key=lambda item: item[1], reverse=True)
        
        return words_count[0][0]
