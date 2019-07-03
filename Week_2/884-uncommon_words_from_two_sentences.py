"""
Two counters are powerful for keeping track of word counts in this question.
"""

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(" ")
        B = B.split(" ")
        
        A_counter = Counter(A)
        B_counter = Counter(B)
        
        
        uncommon_words = []
        
        for key in A_counter:
            if A_counter[key] == 1 and B_counter[key] == 0:
                uncommon_words.append(key)

        for key in B_counter:
            if B_counter[key] == 1 and A_counter[key] == 0:
                uncommon_words.append(key)
                
        return uncommon_words
