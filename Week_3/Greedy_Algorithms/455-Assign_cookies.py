"""
Sorting both arrays is important as it is important for the algorithm to optimize greedily. My solution is to implement a counter that gradually shrinks in size as cookies are "removed" from the jar. I made a new list from the counter dictionary's keys so that I would not get a size change error.
"""

from collections import Counter

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        jar = Counter(s)
        
        satisfied = 0
        for i in range(len(g)):
            for cookie in list(jar.keys()):
                if cookie >= g[i] and jar[cookie] > 0:
                    if jar[cookie] == 1:
                        del jar[cookie]
                    else:
                        jar.update({cookie: -1})
                    satisfied += 1
                    break
        
        return satisfied 
